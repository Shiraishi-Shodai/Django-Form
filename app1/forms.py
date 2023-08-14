from django import forms 
from .models import OneText

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=100)
    sender = forms.EmailField()
    files = forms.FileField()
    u = forms.URLField()

class Test(forms.ModelForm):
    class Meta:
        model = OneText
        fields = '__all__'