from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput

from main.models import Certificate

class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = [
            "title",
            "organization",
            "date",
            "thumbnail",
        ]
        labels = {
            "title": "Judul sertifikat",
            "organization": "Nama organisasi",
            "date" : "Masukkan tanggal rilis sertifikat",
            "thumbnail":"thumbnail sertifikat",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Judul sertifikat",
                    "maxlength": 255,
                }
            ),
            "organization": TextInput(
                attrs={
                    "placeholder": "Nama organisasi",
                    "maxlength": 255,
                }
            ),
            "date": DateInput(
                attrs={
                    'type' : 'date'
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }