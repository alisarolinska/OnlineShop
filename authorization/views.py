from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from authorization.forms import UserForm, RegisterForm


def authorization(request):
	context = {
		'form': UserForm(),
		'error': None,
		'is_authenticated': request.user.is_authenticated,
		'user': request.user
	}
	if request.method == 'GET':
		return render(request, 'login.html', context)
	if request.method == 'POST':
		form = UserForm(request.POST)
		user = authenticate(
			username=form.data['username'],
			password=form.data['password']
		)
		if user is None:
			context['error'] = 'Invalid username or password'
			return render(request, 'login.html', context)
		else:
			login(request, user)
			return redirect('home')


def registration(request):
	context = {
		'form': RegisterForm(),
		'error': None
	}
	if request.method == 'GET':
		return render(request, 'register.html', context)  # Вывести форму на страницу
	elif request.method == 'POST':
		form = RegisterForm(request.POST)
		has_user = User.objects.filter(username=form.data['username']).exists()
		if has_user:
			context['error'] = 'User with this username already exists'
			return render(request, 'register.html', context)
		if len(form.data['password']) < 6:
			context['error'] = 'Password must be at least 6 characters long'
			return render(request, 'register.html', context)
		if form.data['password'] != form.data['password2']:
			context['error'] = 'Passwords do not match'
			return render(request, 'register.html', context)
		password = make_password(form.data['password'])
		user = User.objects.create(
			username=form.data['username'],
			email=form.data['email'],
			password=password
		)
		return redirect('home')


def logout_user(request):
	logout(request)
	return redirect('login')
