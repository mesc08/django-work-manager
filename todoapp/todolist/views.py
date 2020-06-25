from django.shortcuts import render,, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from .forms import TodoForm
from .models import todolist
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	return render(request,'todolist/home.html')
def login(request):
	if request.method == 'GET':
		return render(request,'todolist/login.html',{'form':UserCreationForm()})
	else:
		if request.POST['password1']==request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('currentlist')
			except IntegrityError:
				context = {
					'form': UserCreationForm(),
					'error': 'username already exist',
				}
				return render(request,'todolist/register.html', context)
		else:
			context = {
				'form': UserCreationForm(),
				'error': "password did not match",
			}