""" This email field is taken from
    https://gist.github.com/CptLemming/e70d01c8598e1dd3957f
"""
from django import forms
from django.core.validators import validate_email, EMPTY_VALUES
from django.utils.translation import ugettext_lazy as _


class EmailListField(forms.Field):
    description = _('Email addresses')

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(EmailListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if value in EMPTY_VALUES:
            return []

        value = [
            item.strip() for item in value.split(self.token) if item.strip()]

        return list(set(value))

    def clean(self, value):
        """
        Check that the field contains one or more 'comma-separated' emails
        and normalizes the data to a list of the email strings.
        """
        value = self.to_python(value)

        if value in EMPTY_VALUES and self.required:
            raise forms.ValidationError(_('This field is required.'))

        for email in value:
            try:
                validate_email(email)
            except forms.ValidationError:
                raise forms.ValidationError(
                    _("'%s' is not a valid email address.") % email)
        return ",".join(value)
