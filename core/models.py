from django.db import models
from django.utils import timezone

EMAIL_STATUS = (
    (0, 'Pending'),
    (1, 'Sent'),
    (2, 'Failed'),
)


class EmailQueue(models.Model):

    PENDING = 0
    SENT = 1
    FAILED = 2

    from_address = models.EmailField()

    to_address = models.CharField(max_length=1024)

    subject = models.CharField(max_length=256, blank=True, null=True)

    body = models.TextField()

    when = models.DateTimeField(auto_now_add=True)

    status = models.IntegerField(choices=EMAIL_STATUS, default=0)

    remarks = models.TextField(null=True, blank=True)

    when_sent = models.DateTimeField(null=True, blank=True)

    @property
    def when_sent_isoformat(self):
        if self.when_sent:
            return self.when_sent.strftime("%Y-%m-%d %H:%M")
        return 'Not Sent'

    def mark_sent(self):
        self.status = EmailQueue.SENT
        self.when_sent = timezone.now()
        self.save(update_fields=['status', 'when_sent'])

    def mark_failed(self, reasons):
        self.status = EmailQueue.FAILED
        self.remarks = reasons
        self.when_sent = timezone.now()
        self.save(update_fields=['status', 'when_sent', 'remarks'])

    class Meta:
        ordering = ['-when']
