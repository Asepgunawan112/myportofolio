from django.urls import path
from main import api_views

app_name = "api"
urlpatterns = [
    path("book/", api_views.book_list, name="book-list"),
    path("book/<uuid:book_id>/", api_views.book_detail, name="book-detail"),
    path("book/<uuid:project_id>/", api_views.book_detail, name="book-detail"),
    path("projects/<uuid:book_id>/star/", api_views.book_star, name="book-star"),
    path("certificate/", api_views.certificate_list, name="certificate-list"),
    path(
        "certificate/<uuid:certificate_id>/",
        api_views.certificate_detail,
        name="certificate-detail",
    ),
    path(
        "certificate/<uuid:certificate_id>/star/",
        api_views.certificate_star,
        name="certificate-star",
    ),
    path("experience/", api_views.experience_list, name="experience-list"),
    path(
        "experience/<uuid:experience_id>/",
        api_views.experience_detail,
        name="experience-detail",
    ),
    path(
        "experience/<uuid:experience_id>/star/",
        api_views.experience_star,
        name="experience-star",
    ),
]