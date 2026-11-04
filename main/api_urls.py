from django.urls import path
from main import api_views

app_name = "api"
urlpatterns = [
    path("book/", api_views.book_list, name="book-list"),
    path("book/<uuid:book_id>/", api_views.book_detail, name="book-detail"),
    path("book/<uuid:project_id>/", api_views.book_detail, name="book-detail"),
    path("projects/<uuid:book_id>/star/", api_views.book_star, name="book-star"),
]