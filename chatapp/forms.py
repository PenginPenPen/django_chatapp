from django import forms
from .models import chat
class chatForm(forms.ModelForm):
    class Meta:
        model = chat
        name = forms.CharField(max_length=20,initial='name')
        message = forms.CharField(max_length=1000,initial='message')
        # file = forms.FileField()
        fields = ['name', 'message']