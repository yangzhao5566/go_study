from celery import Celery

brokers = 'redis://127.0.0.1:6379/5'
backend = 'redis://127.0.0.1:6379/6'

app = Celery("tasks", broker=brokers, backend=backend)

@app.task
def add(x, y):
    return x + y


r = add.apply_async(args=[3, 5], countdown=60)

