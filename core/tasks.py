from __future__ import absolute_import, unicode_literals

from pydoc import locate
from django.conf import settings

from core.models import EmailQueue
from celery import task


EMAIL_PROVIDER = locate(settings.EMAIL_PROVIDER)
Sender = EMAIL_PROVIDER()


@task()
def send_email():
    email_queues = EmailQueue.objects.filter(
        status=EmailQueue.PENDING)[:settings.EMAIL_RATE_LIMIT]
    for email in email_queues:
        print('sending email {}'.format(email.from_address))
        Sender.send(email)
