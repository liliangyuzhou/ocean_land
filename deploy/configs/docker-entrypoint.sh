#!/bin/sh
set -e
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('liliang', '1287641566@qq.com', '123456')" | python manage.py shell &> /dev/null
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('liliang1', '1287641567@qq.com', '123456')" | python manage.py shell &> /dev/null

/usr/local/bin/gunicorn -c /usr/src/app/configs/gunicorn_config.py ocean_land.wsgi
