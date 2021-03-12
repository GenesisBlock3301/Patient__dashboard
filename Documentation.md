# Create Virtual Environment
```
conda create -n patientDash python=3.8
```

## Activate virtual Environment
```
conda activate patientDash
```
# Django setup and run
```
pip install django
django-admin startproject patientDash
python manage.py startapp Dashboard
python manage.py createsuperuser
```
### Run django APP
```
python manage.py runserver
```

#### setup postgresql
runserver and config

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'patientDB',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```



