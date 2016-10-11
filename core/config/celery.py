from datetime import timedelta
#from celery.schedules import crontab

# For message brokers in Celery - Using Rabbit MQ now
BROKER_URL = 'amqp://nirlendu:nirlendu@localhost:5672/vhost'

# Some temp setting, will come back to this later
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'

CELERYBEAT_SCHEDULE = {
    'test-celery-task': {
        'task': 'app_base.views.celery_test',
        'schedule': timedelta(seconds=5),
    },
}