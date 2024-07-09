from django.contrib.auth.models import Group, User
from rest_framework import serializers

from taskapp.models import  TaskModel


class TaskSerializer(serializers.ModelSerializer):


    class Meta:
        model = TaskModel
        fields = ('id', 'title', 'description', 'assigned_to', 'due_date', 'priority', 'category', 'subtasks','bucket')