
from django.contrib import admin
from django.urls import path, include
from todolist import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Autherisation
    path('register/',views.registeruser, name='registeruser'),
    path('login/',views.loginuser, name='loginuser'),
    path('logout/',views.logoutuser, name='logoutuser'),
    
    #Todolist
    path('',views.home,name='home'),
    path('createtodolist/',views.createtodolist, name='createtodolist'),
    path('currenttodolist/',views.currenttodolist, name='currenttodolist'),
    path('completedtodolist/',views.completedtodolist,name='completedtodolist'),
    path('todolist/<int:todolist_pk>',views.displaytodolist,name='displaytodolist'),
    path('todolist/<int:todolist_pk>/completetodolist',views.completetodolist, name='completetodolist'),
    path('todolist/<int:todolist_pk>/deletetodolist',views.deletetodolist,name='deletetodolist'),
    path('api/', include('todolist.urls')),
]
