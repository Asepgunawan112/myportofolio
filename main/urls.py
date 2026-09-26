from django.urls import path

from main.views import show_main, show_experience, show_certificate, create_certificate, get_certificate_json, delete_certificate, show_book, create_book, delete_book, get_book_json, edit_book_data, edit_certificate_data, create_experience, edit_experience_data, delete_experience, get_experience_json, get_certificate_json, register, login_user, logout_user, toggle_star_book, toggle_star_experience, toggle_star_certificate

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("certificate/add", create_certificate, name="create_certificate"), 
    path("experience/", show_experience, name="show_experience"),
    path("experience/add", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/edit/", edit_experience_data, name="edit_experience_data"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("certificate/", show_certificate, name="show_certificate"),
    path("api/certificate/", get_certificate_json, name="get_certificate_json"),
    path("certificate/<uuid:certificate_id>/delete/",delete_certificate,name="delete_certificate"),
    path("book/", show_book, name="show_book"),
    path("book/add", create_book, name="create_book"),
    path("api/book/", get_book_json, name="get_book_json"),
    path("book/<uuid:book_id>/delete/", delete_book, name="delete_book"),
    path("book/<uuid:book_id>/edit/", edit_book_data, name="edit_book_data"),
    path("certificate/<uuid:certificate_id>/edit/", edit_certificate_data, name="edit_certificate_data"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("book/<uuid:book_id>/star/",toggle_star_book,name="toggle_star_book"),
    path("certificate/<uuid:certificate_id>/star/",toggle_star_certificate,name="toggle_star_certificate"),
    path("experience/<uuid:experience_id>/star/",toggle_star_experience,name="toggle_star_experience"),
]       