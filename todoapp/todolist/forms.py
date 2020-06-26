from django.forms import ModelForm
from .models import todolist

class TodoForm(ModelForm):
	class Meta:
		model =  todolist
		fields = ['title','description','priority']