from __future__ import absolute_import, unicode_literals

import logging
from pydoc import locate
from appemail.celery import app
from django.conf import settings

# from core.utils import MailGunSender as EMAIL_PROVIDER
from core.models import EmailQueue

EMAIL_PROVIDER = locate(settings.EMAIL_PROVIDER)
Sender = EMAIL_PROVIDER()


@app.task
def send_email(email_queue):
    # email_queues = EmailQueue.objects.filter(
    #     status=EmailQueue.PENDING)[:settings.EMAIL_RATE_LIMIT]
    # for email in email_queues:
    # print('sending email {}'.format(email.from_address))
    email = EmailQueue.objects.filter(pk=email_queue).first()
    if email:
        Sender.send(email)
        return
    logging.error('Email not found')
