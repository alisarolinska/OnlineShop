from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email']