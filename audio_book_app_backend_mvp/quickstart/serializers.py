from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Books
        fields = ('book_id', 'book_title', 'author_name', 'published_year', 'folder_name', 'number_of_episodes')


class ChaptersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Chapters
        fields = ('chapter_id', 'chapter_title', 'book')
