# rzeczuchyBlog
Repository for the rzeczuchyBlog app.

## Starting app using Pipenv
For this method you'll need [Pipenv](https://pypi.org/project/pipenv/). This is the workflow I'd recommend for running the app.

To run the app, clone the repository. In the root folder (where `Pipfile` is located) install packages using Pipenv:
```
$ pipenv install
```

Activate the Pipenv shell:
```
$ pipenv shell
```

Once the Pipenv shell is activated, go from the root to the `rzeczuchyBlog` folder, where the `manage.py` file is located.

From there you will need to run the migrations:
```
python manage.py migrate
```

Once the migrations are completed, you can start the app using:
```
python manage.py runserver
```

The development server should by default start at port 8000. You can specify a different port like so:
```
python manage.py runserver [port]
```

To access the admin area, you will need to create the superuser with:
```
python manage.py createsuperuser
```

## Notices
This app makes use of the Django framework for Python:\
https://github.com/django/django

For rich-text editing, the Django CKEditor integration has been used:\
https://github.com/django-ckeditor/django-ckeditor