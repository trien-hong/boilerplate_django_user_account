from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class Login(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder':'Enter your username', 'size':'25'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password', 'size':'25'}))

class Signup(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder':'Enter your username', 'size':'25'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password', 'size':'25'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm your password', 'size':'25'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exist.')
        return username
    
    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
        return password