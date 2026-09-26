from django.shortcuts import render, redirect
from main.models import Experience, Certificate, Book
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.form import CertificateForm, BookForm, ExperienceForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied        
import datetime


def show_main(request): #fungsi halaman utama
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Ayyasi",
        "npm": "2506550482",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "2nd-year Computer Science student at Universitas Indonesia."
            "Interested in web development and currently still learning more. I"
            "am Sundanese."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def show_experience(request): #show mamakai json
    json_response = get_experience_json(request)

    experience = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"), 
        use_natural_foreign_keys=True
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

@login_required(login_url="/login/")
def create_experience(request): #fungsi tambah pengalaman

    if not request.user.is_superuser:
        raise PermissionDenied
    form = ExperienceForm(request.POST or None)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        experience = Experience(title=title, description=description)
        experience.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")
    

    context = {
        "name": "Ayyasi",
        "form" : form,
    }
    return render(request, "experience_form.html", context)


def get_experience_json(request): #fungsi ambil data pengalaman
    experience = Experience.objects.all()
    experience_json = serializers.serialize("json", experience,  use_natural_foreign_keys=True)
    return HttpResponse(experience_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_experience(request, experience_id): #fungsi hapus data pengalaman
    if not request.user.is_superuser:
        raise PermissionDenied

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

@login_required(login_url="/login/")
def create_certificate(request): #fungsi tambah sertifikat
    if not request.user.is_superuser:
        raise PermissionDenied

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

@login_required(login_url="/login/")
#fungsi delete  data
def delete_certificate(request, certificate_id):

    if not request.user.is_superuser:
        raise PermissionDenied
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

@login_required(login_url="/login/")
def create_book(request): #fungsi tambah buku
    if not request.user.is_superuser:
        raise PermissionDenied

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

@login_required(login_url="/login/")
def delete_book(request, book_id): #fungsi haous data buku
    if not request.user.is_superuser:
        raise PermissionDenied

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

    book_json = serializers.serialize("json", book,  use_natural_foreign_keys=True)
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

    # views register
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request): # views login
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Ayyasi",
        "form": form,
    }
    return render(request, "login.html", context)
    
#views logout
def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in book.starred_by.all():
            book.starred_by.remove(request.user)
        else:
            book.starred_by.add(request.user)

    return redirect("main:show_book")

@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_star_certificate(request, certificate_id):
    certificate = get_object_or_404(Certificate, pk=certificate_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in certificate.starred_by.all():
            certificate.starred_by.remove(request.user)
        else:
            certificate.starred_by.add(request.user)

    return redirect("main:show_certificate")