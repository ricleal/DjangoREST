# start

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

My project
```
cd mine
django-admin.py startproject tutorial .
jango-admin.py startapp restaurantapi

├── manage.py
├── restaurantapi
│   ├── __init__.py
│   ├── admin.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── tutorial
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver --noreload # no reload changes


```

Once REST api running do:
http://localhost:8000/
http://localhost:8000/user/

For XML renderers
http://localhost:8000/?format=xml

See available menus
http://localhost:8000/available_menus/
