from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Book, Certificate, Experience
from main.permissions import IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import (
    bookSerializer, certificateSerializer, experienceSerializer,
)


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
        return Response(status=status.HTTP_204_NO_CONTENT)
    book.starred_by.add(request.user)
    serializer = bookSerializer(book, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def certificate_list(request):
    if request.method in ("GET", "HEAD"):
        certificates = Certificate.objects.prefetch_related(
            "starred_by",
        ).order_by("title", "id")
        title = request.query_params.get("title", "").strip()
        if title:
            certificates = certificates.filter(title__icontains=title)
        serializer = certificateSerializer(
            certificates, many=True, context={"request": request},
        )
        return Response(serializer.data)

    serializer = certificateSerializer(
        data=request.data, context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def certificate_detail(request, certificate_id):
    certificate = get_object_or_404(
        Certificate.objects.prefetch_related("starred_by"),
        pk=certificate_id,
    )
    if request.method in ("GET", "HEAD"):
        serializer = certificateSerializer(
            certificate, context={"request": request},
        )
        return Response(serializer.data)

    if request.method == "DELETE":
        certificate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = certificateSerializer(
        certificate, data=request.data,
        partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def certificate_star(request, certificate_id):
    certificate = get_object_or_404(Certificate, pk=certificate_id)
    if certificate.starred_by.filter(pk=request.user.pk).exists():
        certificate.starred_by.remove(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
    certificate.starred_by.add(request.user)
    serializer = certificateSerializer(
        certificate, context={"request": request},
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def experience_list(request):
    if request.method in ("GET", "HEAD"):
        experiences = Experience.objects.prefetch_related(
            "starred_by",
        ).order_by("title", "id")
        title = request.query_params.get("title", "").strip()
        if title:
            experiences = experiences.filter(title__icontains=title)
        serializer = experienceSerializer(
            experiences, many=True, context={"request": request},
        )
        return Response(serializer.data)

    serializer = experienceSerializer(
        data=request.data, context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def experience_detail(request, experience_id):
    experience = get_object_or_404(
        Experience.objects.prefetch_related("starred_by"),
        pk=experience_id,
    )
    if request.method in ("GET", "HEAD"):
        serializer = experienceSerializer(
            experience, context={"request": request},
        )
        return Response(serializer.data)

    if request.method == "DELETE":
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = experienceSerializer(
        experience, data=request.data,
        partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def experience_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if experience.starred_by.filter(pk=request.user.pk).exists():
        experience.starred_by.remove(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
    experience.starred_by.add(request.user)
    serializer = experienceSerializer(
        experience, context={"request": request},
    )
    return Response(serializer.data, status=status.HTTP_200_OK)