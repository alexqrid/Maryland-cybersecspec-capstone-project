from django import forms
from .models import Message


class MessageCreationForm(forms.ModelForm):
    sender = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Message
        fields = ['recipient', 'content']