from datetime import timedelta
#from celery.schedules import crontab

# For message brokers in Celery - Using Rabbit MQ now
BROKER_URL = 'amqp://nirlendu:nirlendu@localhost:5672/vhost'

# Some temp setting, will come back to this later
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'

CELERY_IMPORTS = (
    "cache_operations.views",
)

CELERYBEAT_SCHEDULE = {
    'update_graph_cache': {
        'task': 'cache_operations.views.update_graph_cache',
        'schedule': timedelta(seconds=5),
    },
}