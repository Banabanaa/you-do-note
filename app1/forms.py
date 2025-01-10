from django import forms
from .models import Note
from .models import Task

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']  

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']