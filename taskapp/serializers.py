from django.contrib.auth.models import Group, User
from rest_framework import serializers
from taskapp.models import  TaskModel
from .models import Profile

class TaskSerializer(serializers.ModelSerializer):


    class Meta:
        model = TaskModel
        fields = ('id', 'title', 'description', 'assigned_to', 'due_date', 'priority', 'category', 'subtasks','bucket')


        

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['color', 'initials']



class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user