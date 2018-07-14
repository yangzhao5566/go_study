from celery import Celery
import random
import time

brokers = 'redis://127.0.0.1:6379/5'
backend = 'redis://127.0.0.1:6379/6'

celery = Celery("tasks", broker=brokers, backend=backend)


@celery.task(bind=True)
def long_task(self):
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)

    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(
                random.choice(verb), random.choice(adjective),
                random.choice(noun))
            self.update_state(state="PROGRESS", meta={
                'current': i, 'total': total, 'status': message})
            time.sleep(1)

    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}


@celery.task(bind=True)
def long_time(self):
    i = 0
    while i < 100:
        i += 1
        self.update_state(state="PROGRESS", meta={"i": i})
        time.sleep(0.2)
    return "finished"
