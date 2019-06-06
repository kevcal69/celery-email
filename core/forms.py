from django import forms

from core.fields import EmailListField
from core.models import EmailQueue


class EmailQueeForms(forms.ModelForm):
    to_address = EmailListField()

    class Meta:
        model = EmailQueue
        fields = ('from_address', 'to_address', 'subject', 'body')
