from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'todolist/home.html')


def registeruser(request):
    if request.method == 'GET':
        return render(request, 'todolist/register.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodolist')
            except IntegrityError:
                context = {
                    'form': UserCreationForm(),
                    'error': 'username already exist',
                }
                return render(request, 'todolist/register.html', context)
        else:
            context = {
                'form': UserCreationForm(),
                'error': "password did not match",
            }
            return render(request, 'todolist/register.html', context)


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todolist/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todolist/login.html',
                          {'form': AuthenticationForm(), 'error': 'username and password did not match'})
        else:
            login(request, user)
            return redirect('currenttodolist')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'todolist/home.html')


@login_required
def createtodolist(request):
    if request.method == 'GET':
        return render(request, 'todolist/createtodolist.html', {'form': TodoForm()})
    else:
        try:
            todos = TodoForm(request.POST)
            new_todo = todos.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('currenttodolist')
        except ValueError:
            return render(request, 'todolist/createtodolist.html', {'form': TodoForm(), 'error': 'Bad Value'})


@login_required
def currenttodolist(request):
    todos = todolist.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'todolist/currentlist.html', {'todos': todos})


@login_required
def displaytodolist(request, todolist_pk):
    todos = get_object_or_404(todolist, pk=todolist_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todos)
        return render(request, 'todolist/displaytodo.html', {'form': form, 'todos': todos})
    else:
        try:
            form = TodoForm(request.POST, instance=todos)
            form.save()
            return redirect('currenttodolist')
        except:
            return render(request, 'todolist/displaytodo.html',
                          {'form': TodoForm(), 'error': 'Bad value passed in', 'todos': todos})


@login_required
def completedtodolist(request):
    todos = todolist.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'todolist/completedlist.html', {'todos': todos})


@login_required
def completetodolist(request, todolist_pk):
    todo = get_object_or_404(todolist, pk=todolist_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodolist')


@login_required
def deletetodolist(request, todolist_pk):
    todo = get_object_or_404(todolist, pk=todolist_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodolist')
