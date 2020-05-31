from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from . import serializers

# Create your views here.
class BooksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that lets users view all the books
    """
    queryset = models.Books.objects.all()
    serializer_class = serializers.BookSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = models.Books.objects.order_by().all()
        genre = self.request.query_params.get('genre', None)
        author = self.request.query_params.get('author', None)
        if genre is not None:
            queryset = queryset.filter(genre=genre)
        if author is not None:
            author = author.replace("_", " ")
            queryset = queryset.order_by().order_by().filter(author_name=author)
        return queryset


class GenresViewSet(viewsets.ModelViewSet):
    """
    API endpoint that lets users view all the books
    """
    queryset = models.Books.objects.order_by().values('genre').distinct()
    serializer_class = serializers.GenreSerializer
    #permission_classes = [permissions.IsAuthenticated]


class AuthorsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that lets users view all the books
    """
    queryset = models.Books.objects.order_by().values('author_name').distinct()
    serializer_class = serializers.AuthorsSerializer
    #permission_classes = [permissions.IsAuthenticated]


class ChaptersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that lets users view chapters for the books
    """
    queryset = models.Chapters.objects.order_by().all()
    serializer_class = serializers.ChaptersSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = models.Chapters.objects.all()
        book = self.request.query_params.get('book', None)
        if book is not None:
            queryset = queryset.order_by().filter(book=book)
        return queryset
