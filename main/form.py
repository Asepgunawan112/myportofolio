from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput, NumberInput

from main.models import Certificate, Book

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

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "year",
            "sinopsis",
            "thumbnail",
            "status",
        ]
        labels = {
            "title": "Judul buku",
            "author": "Nama penulis",
            "year" : "Tahun terbit",
            "sinopsis":"Sinopsis buku",
            "thumbnail":"Thumbnail buku",
            "status":"Status buku"
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Judul buku",
                    "maxlength": 255,
                }
            ),
            "author": TextInput(
                attrs={
                    "placeholder": "Nama penulis",
                    "maxlength": 255,
                }
            ),
            "year": NumberInput(
                attrs={
                    'type' : 'number',
                    'min' : 0,
                    'max' : 9999,
                }
            ),
            "sinopsis": Textarea(
                attrs={
                    'placeholder': 'Sinopsis buku',
                    'rows': 4,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }