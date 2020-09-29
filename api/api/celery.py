import os
import pprint

from celery import Celery
from celery.signals import task_failure
from django.core.mail import mail_admins, get_connection
from django.template.loader import get_template

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

app = Celery('api', include='desecapi.mail_backends')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@task_failure.connect()
def task_failure(task_id, exception, args, kwargs, traceback, einfo, **other_kwargs):
    context = {
        'task_id': task_id,
        'exception': str(exception),
        'exception_type': str(type(exception)),
        'exception_dict': pprint.pformat(exception.__dict__),
        'task_args': str(args),
        'task_kwargs': pprint.pformat(kwargs),
        'einfo': str(einfo),
        'sender': str(other_kwargs.get('sender', '')),
    }
    subject = get_template(f'emails/exception-celery/subject.txt').render(context).strip()
    print(subject, task_id, exception, args, kwargs, traceback, einfo, other_kwargs)
    mail_admins(
        subject=subject,
        message=get_template('emails/exception-celery/content.txt').render(context),
        connection=get_connection('django.core.mail.backends.smtp.EmailBackend'),
    )
