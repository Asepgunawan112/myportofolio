from django.shortcuts import render
from main.models import Experience, Certificate
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.form import CertificateForm

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
    