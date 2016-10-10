init-env:
	virtualenv env --system-site-packages
server-start:
	python manage.py collectstatic
	sudo nginx
	gunicorn -c server/gunicorn.conf.py core.wsgi
dev-server:
    export DJANGO_SETTINGS_MODULE=core.settings.local
	python manage.py runserver
heroku-server:
    export DJANGO_SETTINGS_MODULE=core.settings.heroku
	python manage.py runserver
staging-server:
    export DJANGO_SETTINGS_MODULE=core.settings.staging
	python manage.py runserver
prod-server:
    export DJANGO_SETTINGS_MODULE=core.settings.production
	python manage.py runserver

