import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'News_Portal.settings')

app = Celery('News_Portal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# Добавляем настройку для устранения предупреждения о депрекации
app.conf.broker_connection_retry_on_startup = True

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'news_portal.tasks.weekly_send_email_task',
        'schedule': crontab(),
        'args': ()
    }
}

