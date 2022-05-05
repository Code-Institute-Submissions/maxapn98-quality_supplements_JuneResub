from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field


class ContactForm(forms.Form):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)

    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = 'post'
        self.helper.form_action = '/contact'

        self.helper.add_input(Submit('submit', 'Submit'))
