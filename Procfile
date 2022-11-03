release: python manage.py migrate
web: gunicorn djangoproject.wsgi
worker: python manage.py qcluster