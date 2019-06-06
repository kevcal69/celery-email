import json

from django.http import HttpResponse
from django.views.generic import View

from core.forms import EmailQueeForms
from core.models import EmailQueue
from core.tasks import send_email


class EmailView(View):

    size_per_request = 15

    def serialize_email_queue(self, emailqueue):
        return {'id': emailqueue.pk,
                'status': emailqueue.get_status_display(),
                'from_address': emailqueue.from_address,
                'to_address': emailqueue.to_address,
                'subject': emailqueue.subject,
                'body': emailqueue.body,
                'when_sent': emailqueue.when_sent_isoformat}

    def get(self, request, *args, **kwargs):
        top = request.GET.get('top', 0)

        queryset = EmailQueue.objects.all()[top:self.size_per_request]

        dataset = [
            self.serialize_email_queue(item)
            for item in queryset
        ]

        return HttpResponse(json.dumps(dataset), status=200)

    def post(self, request, *args, **kwargs):
        form = EmailQueeForms(request.POST or None)
        if form.is_valid():
            instance = form.save()
            send_email.apply_async(args=(instance.pk, ), countdown=2)
            return HttpResponse('Success', status=200)
        else:
            return HttpResponse('error', status=404)
