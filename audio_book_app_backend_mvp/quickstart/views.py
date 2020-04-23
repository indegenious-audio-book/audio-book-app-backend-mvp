from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import render
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


class GenresViewSet(viewsets.ModelViewSet):
    """
    API endpoint that lets users view all the books
    """
    queryset = models.Genres.objects.all()
    serializer_class = serializers.BookSerializer
    #permission_classes = [permissions.IsAuthenticated]
