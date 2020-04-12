from django.db import models

# Create your models here.
class Books(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_title = models.CharField(max_length=100, primary_key=True)
    author_name = models.CharField(max_length=100)
    published_year = models.IntegerField()


class Chapters(models.Model):
    chapter_id = models.IntegerField(primary_key=True)
    chapter_title = models.CharField(max_length=100, primary_key=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)



