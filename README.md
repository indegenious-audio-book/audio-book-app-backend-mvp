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
* http://127.0.0.1:8000/api/v1/chapters/?book=1 for getting the list of chapters for the book

# docs

we will get list of genres in this [genres.md](genres_list.md)
