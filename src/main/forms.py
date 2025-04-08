from django import forms


class EmailForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-group", "placeholder": "Name", 'id': "name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control", "placeholder": "Email"}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", "placeholder": "Message"}))