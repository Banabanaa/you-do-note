from django import forms
from .models import Note
from .models import Task

# Form for the notes
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']  

# Form for the tasks
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']