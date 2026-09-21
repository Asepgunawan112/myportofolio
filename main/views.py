from django.shortcuts import render
from main.models import Experience, Certificate, Book
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.form import CertificateForm, BookForm, ExperienceForm


def show_main(request): #fungsi halaman utama
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

def show_experience(request): #show mamakai json
    json_response = get_experience_json(request)

    experience = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experience = [experience.object for experience in experience] 
    
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Ayyasi", 
        "experience_list": experience,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def edit_experience_data(request, experience_id): #fungsi edit data pengalaman
    experience = Experience.objects.get(id=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil diupdate!")
        return redirect("main:show_experience")
    context = {
        "name": "Burhan",
        "form": form,
        "experience": experience,
    }
    return render(request, 'components/edit_experience.html',context)

def create_experience(request): #fungsi tambah pengalaman
    form = ExperienceForm(request.POST or None)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        experience = Experience(title=title, description=description)
        experience.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")
    

    context = {
        "name": "Burhan",
        "form" : form,
    }
    return render(request, "experience_form.html", context)


def get_experience_json(request): #fungsi ambil data pengalaman
    experience = Experience.objects.all()
    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")

def delete_experience(request, experience_id): #fungsi hapus data pengalaman
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def show_certificate(request): # show memakai json
    json_response = get_certificate_json(request)

    certificate = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    certificate = [certificate.object for certificate in certificate] 
    
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Ayyasi", 
        "certificate_list": certificate,
        "title_query": title_query,
    }
    return render(request, "certificate.html", context)

def create_certificate(request): #fungsi tambah sertifikat
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

def edit_certificate_data(request, certificate_id): #fungsi edit data sertifikat
    certificate = Certificate.objects.get(id=certificate_id)
    form = CertificateForm(request.POST or None, instance=certificate)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Certificate berhasil diupdate!")
        return redirect("main:show_certificate")
    context = {
        "name": "Burhan",
        "form": form,
        "certificate": certificate,
    }
    return render(request, 'components/edit_certificate.html',context)

def get_certificate_json(request): #fungsi ambil data sertifikat
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
    json_response = get_book_json(request)

    book = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    book = [book.object for book in book] 
    
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Ayyasi", 
        "book_list": book,
        "title_query": title_query,
    }
    return render(request, "book.html", context)

def create_book(request): #fungsi tambah buku
    form = BookForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Buku baru berhasil ditambahkan!")
        return redirect("main:show_book")

    context = {
        "name": "Ayyasi",
        "form": form,
    }
    return render(request, "book_form.html", context)

def delete_book(request, book_id): #fungsi haous data buku
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        book.delete()
        messages.success(request, "Book berhasil dihapus!")
        return redirect("main:show_book")

    return redirect("main:show_book")

def get_book_json (request): #fungsi ambil data buku
    title_query = request.GET.get("title", "").strip()
    book = Book.objects.all()

    if title_query:
        book = book.filter(title__icontains=title_query)

    book_json = serializers.serialize("json", book)
    return HttpResponse(book_json, content_type="application/json")

def edit_book_data(request, book_id): #fungsi edit data buku
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
    
    