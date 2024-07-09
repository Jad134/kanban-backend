from django.shortcuts import render
from rest_framework import generics
from .models import TaskModel
from .serializers import  TaskSerializer
# Create your views here.
class TaskListCreate(generics.ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
