from django import forms
from crispy_forms.helper import FormHelper

from contact.models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("first_name", "last_name", "email", "subject", "message")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        first_name = forms.CharField(required=True)
        last_name = forms.CharField(required=True)
        email = forms.EmailField(required=True)
        subject = forms.CharField(required=True)
        message = forms.CharField(widget=forms.Textarea, required=True)
        self.helper = FormHelper()

        self.helper.form_method = 'post'
        self.helper.form_action = '/contact'