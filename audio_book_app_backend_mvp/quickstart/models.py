from django.db import models

# Create your models here.
class Books(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    published_year = models.IntegerField()
    folder_name = models.CharField(max_length=100)
    genre = models.IntegerField()
    number_of_chapters = models.IntegerField()
    thumbnail_url = models.CharField(max_length=100)


class Chapters(models.Model):
    chapter_id = models.IntegerField(primary_key=True)
    chapter_title_english = models.CharField(max_length=100)
    chapter_title_vernacular = models.CharField(max_length=100)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    chapter_url = models.CharField(max_length=100)
    chapter_number = models.IntegerField()
