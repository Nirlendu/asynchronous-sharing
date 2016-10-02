server-start:
	python manage.py collectstatic
	sudo nginx
	gunicorn -c server/gunicorn.conf.py core.wsgi
dev-server:
	python manage.py runserver
