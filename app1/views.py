from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Note
from .forms import NoteForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

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


def HomePage(request):
    notes = Note.objects.filter(user=request.user).order_by('-timestamp')  # Fetch notes for logged-in user
    note_id = request.GET.get('edit')  # Check if an 'edit' parameter exists in the URL
    note_to_edit = None  # Default value for editing

    # If an edit id is passed, fetch the note to edit
    if note_id:
        note_to_edit = get_object_or_404(Note, id=note_id, user=request.user)

    form = NoteForm(instance=note_to_edit) if note_to_edit else NoteForm()

    # Handle form submission (create or edit)
    if request.method == 'POST':
        if note_to_edit:  # If editing, pass the note instance to the form
            form = NoteForm(request.POST, instance=note_to_edit)
        else:  # If creating a new note
            form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # Assign the logged-in user to the note
            note.save()
            return redirect('home')  # Redirect after saving

    return render(request, 'home.html', {'notes': notes, 'form': form, 'note_to_edit': note_to_edit})

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return redirect('home') 

def LogoutPage(request):
    logout(request)
    return redirect('login')