"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todolist import views
urlpatterns = [
    path('admin/', admin.site.urls),

    #Autherisation
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('register/',views.register, name='register')

    #Todolist
    path('',views.home,name='home'),
    path('createlist/',views.createlist, name='createtodo'),
    path('currentlist/',views.currentlist, name='currentlist'),
    path('completedlist/',views.completedlist,name='completedlist'),
    path('todolist/<int:todolist_pk>',views.displaytodo,name='displaytodo'),
    path('todolist/<int:todolist_pk>/complete',views.completetodo, name='completetodo'),
    path('todolist/<int:todolist_pk>/delete',views.deletetodo,name='deletetodo'),
]
