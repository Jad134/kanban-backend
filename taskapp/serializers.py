from django.contrib.auth.models import Group, User
from rest_framework import serializers

from taskapp.models import SubtaskModel, TaskModel

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubtaskModel
        fields = ('id', 'title', 'done')

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, read_only=True)

    class Meta:
        model = TaskModel
        fields = ('id', 'title', 'description', 'assigned_to', 'due_date', 'priority', 'category', 'subtasks','bucket')