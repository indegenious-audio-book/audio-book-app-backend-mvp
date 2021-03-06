# Generated by Django 3.0.5 on 2020-04-14 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('published_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('chapter_id', models.IntegerField(primary_key=True, serialize=False)),
                ('chapter_title', models.CharField(max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.Books')),
            ],
        ),
    ]
