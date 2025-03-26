from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterForm(UserCreationForm):
    firstname = forms.CharField(max_length=50, required=True)
    lastname = forms.CharField(max_length=50, required=False)
    phone = forms.CharField(max_length=20, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(required=False)
    bio = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "firstname",
            "lastname",
            "phone",
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control", "placeholder": "Username"}),
            'password1': forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Password"}),
            'password2': forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Confirm Password"}),
        }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.firstname = self.cleaned_data.get('firstname')
        user.lastname = self.cleaned_data.get('lastname')
        user.phone = self.cleaned_data.get('phone')
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                firstname=self.cleaned_data.get('firstname'),
                lastname=self.cleaned_data.get('lastname'),
                phone=self.cleaned_data.get('phone'),
            )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Username"}))
    password = forms.CharField(max_length=20,
                               widget=forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Password"}))
