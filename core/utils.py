import requests
import logging


from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from core.models import EmailQueue


class SendEmail(object):

    def send_queued_email(self, queued_email):
        print('sending queued email {}'.format(queued_email.pk))
        return EmailQueue.SENT

    def send(self, queued_email):
        results, reasons = self.send_queued_email(queued_email)
        if results:
            queued_email.mark_sent()
        else:
            queued_email.mark_failed(str(reasons))


class MailGunSender(SendEmail):

    def __init__(self, *args, **kwargs):
        if not hasattr(settings, 'MAILGUN_API_URL') or\
                not settings.MAILGUN_API_URL:
            raise ImproperlyConfigured(
                'The settings variable MAILGUN_API_URL is not set. The'
                'MAILGUN_API_URL is the base url for mailgun api url.'
                'e.g. https://api.mailgun.net/v3/mg.vipsai.com/messages')
        if not hasattr(settings, 'MAILGUN_API_KEY') or\
                not settings.MAILGUN_API_KEY:
            raise ImproperlyConfigured(
                'The settings variable MAILGUN_API_KEY is not set.')
        return super(MailGunSender, self).__init__(*args, **kwargs)

    def send_queued_email(self, queued_email):
        post_args = {
            'from': queued_email.from_address,
            'to': queued_email.to_address,
            'subject': queued_email.subject,
            'html': queued_email.body
        }
        r = requests.post(
            settings.MAILGUN_API_URL,
            auth=('api', settings.MAILGUN_API_KEY), data=post_args)
        print(r.status_code)
        print(r.content)
        if r.status_code != 200:
            logging.error(
                'Email has not been sent.' +
                'from: {}'.format(post_args['from']) +
                'to: {}'.format(post_args['to']))
            return False, r.content
        return True, 'Success'
