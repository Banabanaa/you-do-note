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
    path('admin/', admin.site.urls),
    path('', views.HomePage, name='home'),  # Redirect root URL to home page
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('home_todo/', views.home_todo, name='home_todo'), 
    path('task/<int:task_id>/update_status/<str:status>/', views.update_task_status, name='update_task_status'),
    path('task/<int:task_id>/permanent_delete/', views.permanent_delete_task, name='permanent_delete_task'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('logout/', views.LogoutPage, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
