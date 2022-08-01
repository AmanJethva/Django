from dataclasses import field
import email
from telnetlib import AUTHENTICATION
from tkinter import Widget
from unicodedata import name
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.forms import User
from flexapp import models
from django.utils.translation import gettext, gettext_lazy as _

class SignupForm(UserCreationForm):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'search_text_name'}))
    cname = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'search_text_cname'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'search_text_email'}))
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'search_text_password'}))
    password2 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'search_text_password'}))

    class Meta:
        model = User
        fields = ['username','email','password1']
        labels = {'email':'Email','username':'Name','cname':'Company Name'}
        Widgets = {'username':forms.TextInput(attrs={'class':'name'})}


class LoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'search_text_email'}))
    password = forms.CharField(label=_("Password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'search_text_password'}))