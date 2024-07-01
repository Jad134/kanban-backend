import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TaskModel(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('urgent', 'Urgent'),
    ]
    title= models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField(default=datetime.date.today)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    category = models.CharField(max_length=30)
    
   
    def __str__(self):
        return self.title
    


class SubtaskModel(models.Model):
    task = models.ForeignKey(TaskModel, related_name='subtasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - Done: {self.done}"
