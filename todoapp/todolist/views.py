from django.shortcuts import render,, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from .forms import TodoForm
from .models import todolist
from django.contrib.auth.decorators import login_required
import pdfkit
# Create your views here.
def home(request):
	return render(request,'todolist/home.html')
def registers(request):
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
			return render(request,'todolist/register.html',context)
def logins(request):
	if request.method == 'GET':
		return render(request,'todolist/login.html',{'form': AuthenticationForm()})
	else:
		user = authenticate(request,username=request.POST['username'], password = request.POST['password'])
		if user is None:
			return render(request,'todolist/login.html',{'form':AuthenticationForm(),'error':'username and password did not match'})
		else:
			login(request, user)
			return render('currentlist')

@login_required
def logouts(request):
	id request.method == 'POST':
		logout(request)
		return render(request,'todolist/home.html')

@login_required
def createlist(request):
	if request.method == 'GET':
		return render(request,'todolist/createtodolist.html',{'form':TodoForm()})
	else:
		try:
			todo = TodoForm()
			new_todo = todo.save(commit=False)
			new_todo.user = request.user
			new_todo.save()
			return redirect('currentlist')
		except ValueError:
			return render(request,'todolist/currentlist.html',{'form':TodoForm(),'error':'Bad Value'})
@login_required
def currentlist(request):
	todos = todolist.objects.filter(user=request.user,datecompleted__isnull=True)
	return render(request,'todolist/currentlist.html',{'todos':todos})
@login_required
def displaytodo(request, todolist_pk):
	todo = get_object_or_404(todolist,pk = todolist_pk, user = request.user)
	if request.method =='GET':
		form = TodoForm(instance = todo)
		return render(request,'todolist/displaytodo.html',{'form':form,'todo':todo})
	else:
		try:
			form = TodoForm(request.POST,instance=todo)
			form.save()
			return redirect('currentlist')
		except:
			return render(request,'todolist/displaytodo.html',{'form':TodoForm(),'error':'Bad value passed in','todo': todo})
@login_required
def completedlist(request):
	todos = todolist.objects.filter(user = user.request, datecompleted__isnull=False).order_by('-datedcompleted')
	return render(request,'todolist/completedlist.html',{'todos':todo})

@login_required
def completedtodo(request,todolist_pk):
	todo = get_object_or_404(todolist, pk = todolist_pk, user = request.user)
	if request.method == "POST":
		todo.datedcompleted = timezone.now()
		todolist.save()
		return redirect('currentlist')

@login_required
def deletetodo(request,todolist_pk):
	todo = get_object_or_404(todolist,pk = todolist_pk, user = request.user)
	if request.method=='POST':
		todo.delete()
		return redirect('currentlist')
@login_required
def generatepdf(request):
		return pdfkit.from_file(redirect('completedlist'),'sample.pdf')						