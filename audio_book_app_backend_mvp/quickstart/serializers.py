from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Books
        fields = ('book_id', 'book_title', 'author_name', 'published_year', 'folder_name', 'genre', 'number_of_chapters', 'thumbnail_url')


class ChaptersSerializer(serializers.ModelSerializer):
    book = serializers.IntegerField(source='book.book_id', read_only=True)

    class Meta:
        model = models.Chapters
        fields = ('chapter_id', 'chapter_title', 'book', 'chapter_url', 'chapter_number')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = ('genre', )
