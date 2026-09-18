from django.urls import path

from main.views import show_main, show_experience, show_certificate, create_certificate, get_certificate_json, delete_certificate, show_book, create_book, delete_book, get_book_json

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("certificate/add", create_certificate, name="create_certificate"), 
    path("experience/", show_experience, name="show_experience"),
    path("certificate/", show_certificate, name="show_certificate"),
    path("api/certificate/", get_certificate_json, name="get_certificate_json"),
    path("certificate/<uuid:certificate_id>/delete/",delete_certificate,name="delete_certificate"),
    path("book/", show_book, name="show_book"),
    path("book/add", create_book, name="create_book"),
    path("api/book/", get_book_json, name="get_book_json"),
    path("book/<uuid:book_id>/delete/", delete_book, name="delete_book"),
]       