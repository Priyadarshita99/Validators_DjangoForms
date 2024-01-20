from django import forms
from app.models import *
from django.core import validators

def validate_for_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('Started with a')
    
def validate_for_len(data):
    if len(data)<5:
        raise forms.ValidationError('len is less than 5')
    
class Schoolform(forms.Form):
    Sname=forms.CharField(validators=[validate_for_a,validators.MinLengthValidator(5)])
    Sprincipal=forms.CharField(validators=[validate_for_len])
    Slocation=forms.CharField()
    email=forms.EmailField()
    re_enteremail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['re_enteremail']
        if e!=re:
            raise forms.ValidationError('Invalid email')
    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('bots')


