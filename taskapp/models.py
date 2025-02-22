import datetime
from django.db import models
from django.contrib.auth.models import User



class TaskModel(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('urgent', 'Urgent'),
    ]
    title= models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    assigned_to = models.ManyToManyField('Contact', blank=True)
    due_date = models.DateField(default=datetime.date.today)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    category = models.CharField(max_length=30)
    bucket = models.CharField(max_length=30, default='todo')
    subtasks = models.JSONField(default=list, null=True, blank=True)
   
    def __str__(self):
        return self.title
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=30, blank=True)
    initials = models.CharField(max_length=10, blank=True)


class Contact(models.Model):
    name =  models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False)
    number = models.CharField(max_length=20, blank=False)
    initials =  models.CharField(max_length=10, blank=True)
    color = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name