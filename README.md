# audio-book-app-backend-mvp
this is the backend for the mvp

## how to build this project and test it

1. clone this project.

```
git clone git@github.com:indegenious-audio-book/audio-book-app-backend-mvp.git
```

2. create the virtual environment and install the dependencies

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. create and run the migrations

```
python manage.py createmigrations
python manage.py migrate
```

4. run the app

```
python manage.py runserver
```

5. You should be able to see the api on the browser at `http://127.0.0.1:8000/api/v1/books/`. Create the list of books and then check the api.

## check tables on the database

```
 ~/o/a/audio-book-app-backend-mvp   …  sqlite3 db.sqlite3 
SQLite version 3.26.0 2018-12-01 12:34:55
Enter ".help" for usage hints.
sqlite> .tables
auth_group                  django_admin_log          
auth_group_permissions      django_content_type       
auth_permission             django_migrations         
auth_user                   django_session            
auth_user_groups            quickstart_books          
auth_user_user_permissions  quickstart_chapters       
sqlite> .tables 'quick%'
quickstart_books     quickstart_chapters
sqlite> 
sqlite> select * from quickstart_books;
1|Cosmology in Vedanta: The Physics Correlation|C Radhakrishnan, Gopal K.R.|2017
2|The last man|Mary Wollstonecraft Shelley|1826
```

## views

* http://127.0.0.1:8000/api/v1/
* http://127.0.0.1:8000/api/v1/books/
* http://127.0.0.1:8000/api/v1/books/1 .. 2 and so on for the books
* http://127.0.0.1:8000/api/v1/genres/ for the list of genres
* http://127.0.0.1:8000/api/v1/books/?genre=2 for the genres
* http://127.0.0.1:8000/api/v1/books/?auhor=2 for the authors
* http://127.0.0.1:8000/api/v1/chapters/?book=1 for getting the list of chapters for the book

# docs

we will get list of genres in this [genres.md](genres_list.md)

# flow for user for genres

1. user will go to home page. app will make genres call and will list all the genres

```curl http://34.93.249.161:8000/api/v1/genres/```

this will fetch all the list of genres. lets say the output is below.

```
{"count":2,"next":null,"previous":null,"results":[{"genre":5},{"genre":22}]}
```

so we have overall two genres 5 and 22.

2. once i have the list of genres, i will get the list of books of that genre. lets say the user wants 5. so user will click on 5 and app will make the next api call

```curl http://34.93.249.161:8000/api/v1/books/?genres=5```

the output for this is

```
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "book_id": 1,
      "book_title": "Aesop Fables",
      "author_name": "Aesop",
      "published_year": 1484,
      "folder_name": "aesop_fables",
      "genre": 5,
      "number_of_chapters": 240,
      "thumbnail_url": "aesop_fables.jpg"
    },
    {
      "book_id": 2,
      "book_title": "Twenty Thousand Leagues Under the Sea",
      "author_name": "Jules Verne",
      "published_year": 1870,
      "folder_name": "twenty_thousand_leagues_under_the_sea",
      "genre": 22,
      "number_of_chapters": 24,
      "thumbnail_url": "twenty_thousand_leagues_under_the_sea.jpg"
    }
  ]
}
```

so we have two books: 1 and 2.

3. now user will click on the book, which will move on to the player and the player will have the chapter list. to get the list of chapters, app will make the below call

```curl http://34.93.249.161:8000/api/v1/chapters/?book=1&format=json```

and output will be

```
{
  "count": 6,
  "next": null,
  "previous": null,
  "results": [
    {
      "chapter_id": 1,
      "chapter_title": "The Frogs & the Ox",
      "book": 1,
      "chapter_url": "aesop_fables/ch_001.mp3"
    },
    {
      "chapter_id": 2,
      "chapter_title": "Belling the Cat",
      "book": 1,
      "chapter_url": "aesop_fables/ch_001.mp3"
    }
  ]
}
```

the above is the list of chapters

