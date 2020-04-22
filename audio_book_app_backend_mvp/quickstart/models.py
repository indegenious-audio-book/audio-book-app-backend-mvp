from django.db import models

# Create your models here.
class Books(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    published_year = models.IntegerField()
    folder_name = models.CharField(max_length=100)
    number_of_episodes = models.IntegerField()


class Chapters(models.Model):
    chapter_id = models.IntegerField(primary_key=True)
    chapter_title = models.CharField(max_length=100)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)



