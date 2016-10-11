init-env:
	virtualenv venv --system-site-packages

dev-server-start:
	sudo nginx
	gunicorn -c server/gunicorn.conf.py core.wsgi.local

heroku-server-start:
	sudo nginx
	gunicorn -c server/gunicorn.conf.py core.wsgi.heroku

dev-server:
	export DJANGO_SETTINGS_MODULE='core.settings.local'
	echo $$DJANGO_SETTINGS_MODULE
	python manage.py runserver --settings=core.settings.local

heroku-server:
	export DJANGO_SETTINGS_MODULE=core.settings.heroku
	python manage.py runserver 0.0.0.0:$$PORT --noreload --settings=core.settings.heroku

staging-server:
	export DJANGO_SETTINGS_MODULE=core.settings.staging
	python manage.py runserver

prod-server:
	export DJANGO_SETTINGS_MODULE=core.settings.production
	python manage.py runserver