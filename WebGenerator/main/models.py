from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


class Form(models.Model):
    keywords = models.CharField('Keywords', max_length=30)
    location = models.CharField('Location', max_length=30)
    number = models.IntegerField('Number')

    def __str__(self):
        return self.keywords
        return self.number


class SignUpForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Password must be at least 8 characters long.'



