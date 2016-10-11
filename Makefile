init-env:
	virtualenv env --system-site-packages

server-start:
	python manage.py collectstatic
	sudo nginx
	gunicorn -c server/gunicorn.conf.py core.wsgi

dev-server:
	python manage.py runserver --settings=core.settings.local

heroku-server:
	python manage.py runserver 0.0.0.0:$$PORT --noreload --settings=core.settings.heroku

staging-server:
	python manage.py runserver

prod-server:
	python manage.py runserver