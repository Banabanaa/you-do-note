from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Note, Task
from .forms import NoteForm, TaskForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Check if passwords match
        if pass1 != pass2:
            return render(request, 'signup.html', {'error': "Passwords do not match!"})

        # Check if the username or email already exists
        if User.objects.filter(username=uname).exists():
            return render(request, 'signup.html', {'error': "Username is already taken!"})
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': "Email is already registered!"})

        # Create user and save
        my_user = User(username=uname, email=email)
        my_user.set_password(pass1)  # Hash password
        my_user.save()

        return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': "Username or Password is incorrect!"})
    
    return render(request, 'login.html')


@login_required(login_url='login')
def HomePage(request):
    notes = Note.objects.filter(user=request.user).order_by('-timestamp')  # Fetch notes for logged-in user
    note_id = request.GET.get('edit')  
    note_to_edit = None  # Default value for editing

    # If an edit id is passed, fetch the note to edit
    if note_id:
        note_to_edit = get_object_or_404(Note, id=note_id, user=request.user)

    form = NoteForm(instance=note_to_edit) if note_to_edit else NoteForm()

    # Handle form submission
    if request.method == 'POST':
        if note_to_edit:  
            form = NoteForm(request.POST, instance=note_to_edit)
        else:  # If creating a new note
            form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # Assign the logged-in user to their notes
            note.save()
            return redirect('home')  # Redirect after saving

    return render(request, 'home.html', {'notes': notes, 'form': form, 'note_to_edit': note_to_edit})

def home_todo(request):
    # Fetch tasks for each category
    tasks_active = Task.objects.filter(user=request.user, status='Active')
    tasks_completed = Task.objects.filter(user=request.user, status='Completed')
    tasks_deleted = Task.objects.filter(user=request.user, status='Deleted')

    task_form = TaskForm()

    # Handle POST actions
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add_task':  # Handle task creation
            title = request.POST.get('title')
            description = request.POST.get('description')
            if title:  # Ensure title is not empty
                Task.objects.create(user=request.user, title=title, description=description, status='Active')
                messages.success(request, "Task added successfully!")
            else:
                messages.error(request, "Task title is required!")
            return redirect('home_todo')
        
        elif action == 'complete_task':  # Mark task as completed
            task_id = request.POST.get('task_id')
            task = get_object_or_404(Task, id=task_id, user=request.user)
            task.status = 'Completed'
            task.save()
            messages.success(request, "Task marked as completed!")
            return redirect('home_todo')
        
        elif action == 'delete_task':  # Mark task as deleted
            task_id = request.POST.get('task_id')
            task = get_object_or_404(Task, id=task_id, user=request.user)
            task.status = 'Deleted'
            task.save()
            messages.success(request, "Task marked as deleted!")
            return redirect('home_todo')

        else:
            messages.error(request, "Invalid action!")
            return redirect('home_todo')

    return render(request, 'home_todo.html', {
        'tasks_active': tasks_active,
        'tasks_completed': tasks_completed,
        'tasks_deleted': tasks_deleted,
        'task_form': task_form,
    })

def update_task_status(request, task_id, status):
    # Ensure valid status
    if status not in ['Active', 'Completed', 'Deleted']:
        messages.error(request, "Invalid status update!")
        return redirect('home_todo')

    # Fetch task and update status
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.status = status
    task.save()
    messages.success(request, f"Task status updated to {status}!")
    return redirect('home_todo')

def permanent_delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id, user=request.user, status='Deleted')
        task.delete()
        messages.success(request, "Task permanently deleted!")
    else:
        messages.error(request, "Invalid request method!")
    return redirect('home_todo')

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return redirect('home') 

def LogoutPage(request):
    logout(request)
    return redirect('login')