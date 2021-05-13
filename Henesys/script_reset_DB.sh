#!/bin/bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
find . -name "db.sqlite3" -delete
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('zzin', '', '8639sung')" | python manage.py shell
echo "from django.contrib.auth.models import User; User.objects.create_superuser('hong', '', '8639hong')" | python manage.py shell
echo "from django.contrib.auth.models import User; User.objects.create_user('test', '', '8639test')" | python manage.py shell
