from django import forms
from .models import ContactMainReceivedEmails
class ContactForm(forms.ModelForm):
    # Will get fields from model but overriding message giving widget.
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = ContactMainReceivedEmails
        fields = ['subject', 'body', 'from_email']