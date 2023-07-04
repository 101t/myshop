import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_connection_max_retries = 0
app.conf.broker_connection_retry_on_startup = True
app.autodiscover_tasks()
