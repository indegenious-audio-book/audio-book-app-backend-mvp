# Generated by Django 3.0.5 on 2020-04-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_books_folder_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('genre_id', models.IntegerField(primary_key=True, serialize=False)),
                ('genre_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='genre',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]