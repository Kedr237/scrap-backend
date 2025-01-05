#!/bin/sh

until nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 1
done

cd src

python manage.py migrate

python manage.py shell << EOF
import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = os.getenv("SUPERUSER_USERNAME", "admin")
email = os.getenv("SUPERUSER_EMAIL", "admin")
password = os.getenv("SUPERUSER_PASSWORD", "admin")

if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created successfully.")
else:
    print(f"Superuser with '{username}' or '{email}' already exists.")
EOF

python manage.py test

python manage.py flushexpiredtokens
cron &

gunicorn settings.wsgi:application --bind 0.0.0.0:8000