from django.shortcuts import render
from main.models import Experience, Certificate

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
    context = {
        "name": "Ayyasi",
        "certificate_list": Certificate.objects.all(),
    }
    return render(request, "certificate.html", context)
    