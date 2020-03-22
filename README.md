# DRF example

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

First login into the admin API.

Then:

Once REST api running do:
http://localhost:8000/
http://localhost:8000/user/

For XML renderers
http://localhost:8000/?format=xml

See available menus
http://localhost:8000/available_menus/
