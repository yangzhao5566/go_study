# coding=utf-8
from datetime import timedelta

CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/5"
BROKER_URL = "redis://127.0.0.1:6379/6"

CELERY_TIMEZONE = "Asia/Shanghai"


CELERY_SCHEDULE = {
    "add-every-30-seconds": {
        'task': "proj.task.add",
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    }
}