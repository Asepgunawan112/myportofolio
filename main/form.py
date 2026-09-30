from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput, NumberInput, Select

from main.models import Certificate, Book, Experience

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
            "status": Select(
                attrs={
                    'placeholder': 'Status buku',
                }
            ),
        }
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Judul buku tidak boleh hanya berisi tag HTML.")
        return title

    def clean_author(self):
        return strip_tags(self.cleaned_data["author"]).strip()

    def clean_year(self):
        year = strip_tags(self.cleaned_data["year"]).strip()
        if not year:
            raise ValidationError("Tahun terbit tidak boleh hanya berisi tag HTML.")
        return year

    def clean_sinopsis(self):
        return strip_tags(self.cleaned_data["description"]).strip()

    def clean_thumbnail(self):
        return strip_tags(self.cleaned_data["thumbnail"]).strip()

    def clean_status(self):
        return strip_tags(self.cleaned_data["status"]).strip()



class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields =[
            "title",
            "description",
            "category",
            "started_at",
            "ended_at",
        ]
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Judul pengalaman",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsi pengalaman",
                    "rows": 4,
                }
            ),
            "category": Select(
                attrs={
                    "placeholder": "Kategori pengalaman",
                }
            ),
            "started_at": DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            "ended_at": DateInput(
                attrs={
                    'type': 'date'
                }
            ),
        }