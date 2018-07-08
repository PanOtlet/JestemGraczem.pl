release: python manage.py migrate
release: python manage.py collectstatic
web: gunicorn JestemGraczem.wsgi --log-file -
