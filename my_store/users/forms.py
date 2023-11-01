from django.contrib.auth.forms import AuthenticationForm
from django import forms
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    class Meta:
        model = User
        fields = ('username', 'password')