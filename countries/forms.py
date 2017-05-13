
from django import forms

from .models import WebUser

class LoginForm(forms.Form):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': 'Password'}))

class CommentForm(forms.Form):
	comment = forms.CharField(label="Enter a comment", 
								widget=forms.TextInput(
                                   attrs={'placeholder': 'Comment'}))
