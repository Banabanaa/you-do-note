
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# For database migrations

# Represents the user notes in the database
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Represents the user tasks in the database
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Completed', 'Completed'), ('Deleted', 'Deleted')], default='Active')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        

