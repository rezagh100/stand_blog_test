from django import forms
from django.contrib.auth import authenticate
from .models import User
from django.forms import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100'}))

    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        else:
            raise ValidationError('username or password is wrong')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'username')
