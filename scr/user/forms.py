from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterForm(UserCreationForm):
    firstname = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Firstname"}))
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control", "placeholder": "Email"}))

    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Password"}))
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Password"}))

    class Meta:
        model = User
        fields = ['username', 'firstname', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save()
        if user:
            Profile.objects.create(
                user=user,
                firstname=self.cleaned_data['firstname']
            )
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Username"}))
    password = forms.CharField(max_length=20,
                               widget=forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Password"}))
