"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app1 import views
from django.conf import settings  
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),  # Route for the admin dashboard
    path('', views.HomePage, name='home'),  # Route for the homepage (root URL redirects here) This is the Notes Section
    path('signup/', views.SignupPage, name='signup'),  # Route for the signup page
    path('login/', views.LoginPage, name='login'),  # Route for the login page
    path('home_todo/', views.home_todo, name='home_todo'),  # Route for the homepage displaying ToDo section
    path(
        'task/<int:task_id>/update_status/<str:status>/', 
        views.update_task_status, 
        name='update_task_status'
    ),  # Route for updating the status of a specific task (based on task ID and new status)
    path(
        'task/<int:task_id>/permanent_delete/', 
        views.permanent_delete_task, 
        name='permanent_delete_task'
    ),  # Route for permanently deleting a specific task (based on task ID)
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),  # Route for deleting a specific note (based on note ID)
    path('logout/', views.LogoutPage, name='logout'),  # Route for logging out the user
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Serve static files during development