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
