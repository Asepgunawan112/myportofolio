from django.shortcuts import render
from main.models import Experience, Certificate, Book
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.form import CertificateForm, BookForm

# Create your views here.
def show_main(request):
    context = {
        "name": "Ayyasi",
        "npm": "2506550482",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "2nd-year Computer Science student at Universitas Indonesia."
            "Interested in web development and currently still learning more. I"
            "am Sundanese."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Ayyasi",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_certificate(request):
    json_response = get_certificate_json(request)
    certificate = serializers.deserialize("json", json_response.content.decode("utf-8"))
    certificate= [certificate.object for certificate in certificate]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Ayyasi",
        "certificate_list": Certificate.objects.all(),
    }
    return render(request, "certificate.html", context)

def create_certificate(request):
    form = CertificateForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Sertifikat baru berhasil ditambahkan!")
        return redirect("main:show_certificate")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "certificate_form.html", context)

def get_certificate_json(request):
    title_query = request.GET.get("title", "").strip()
    certificate = Certificate.objects.all()

    if title_query:
        certificate = certificate.filter(title__icontains=title_query)

    certificate_json = serializers.serialize("json", certificate)
    return HttpResponse(certificate_json, content_type="application/json")
    # sudah test di postman dan berhasil (yeyy)

#fungsi delete  data
def delete_certificate(request, certificate_id):
    certificate = get_object_or_404(Certificate, pk=certificate_id)

    if request.method == "POST":
        certificate.delete()
        messages.success(request, "Certificate berhasil dihapus!")
        return redirect("main:show_certificate")

    return redirect("main:show_certificate")

def show_book(request):
    title_query = request.GET.get("title", "").strip()
    book_list = Book.objects.all()
    if title_query:
        book_list = book_list.filter(title__icontains=title_query)

    context = {
        "name": "Ayyasi",
        "book_list": book_list,
        "title_query": title_query,
    }
    return render(request, "book.html", context)

def create_book(request):
    form = BookForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Buku baru berhasil ditambahkan!")
        return redirect("main:show_book")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "book_form.html", context)

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        book.delete()
        messages.success(request, "Book berhasil dihapus!")
        return redirect("main:show_book")

    return redirect("main:show_book")

def get_book_json (request):
    title_query = request.GET.get("title", "").strip()
    book = Book.objects.all()

    if title_query:
        book = book.filter(title__icontains=title_query)

    book_json = serializers.serialize("json", book)
    return HttpResponse(book_json, content_type="application/json")

def edit_book_data(request, book_id):
    book= Book.objects.get(id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Book berhasil diupdate!")
        return redirect("main:show_book")
    context = {
        "name": "Burhan",
        "form": form,
        "book": book,
    }
    return render(request, 'components/edit_book.html',context)
    
    