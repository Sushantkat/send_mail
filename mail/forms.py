from django import forms
from .models import EmailAttachment


class EmailAttachmentForm(forms.ModelForm):
    class Meta:
        model = EmailAttachment
        fields = ['email','image' ]
