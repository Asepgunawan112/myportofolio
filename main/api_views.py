from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Book
from main.permissions import IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import bookSerializer


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def book_list(request):
    if request.method in ("GET", "HEAD"):
        book = Book.objects.prefetch_related("starred_by").order_by("title", "id")
        title = request.query_params.get("title", "").strip()
        if title:
            book = book.filter(title__icontains=title)
        serializer = bookSerializer(
            book, many=True, context={"request": request},
        )
        return Response(serializer.data)

    serializer = bookSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def book_detail(request, book_id):
    book = get_object_or_404(
        Book.objects.prefetch_related("starred_by"), pk=book_id,
    )
    if request.method in ("GET", "HEAD"):
        serializer = bookSerializer(book, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = bookSerializer(
        book, data=request.data, partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def book_star(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if book.starred_by.filter(pk=request.user.pk).exists():
        book.starred_by.remove(request.user)
    else:
        book.starred_by.add(request.user)
    serializer = bookSerializer(book, context={"request": request})
    return Response(serializer.data)