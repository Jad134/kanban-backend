from django.shortcuts import render
from rest_framework import generics
from .models import Contact, TaskModel
from .serializers import  ContactSerializer, TaskSerializer, UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User



class TaskListCreate(generics.ListCreateAPIView):
    """
    Create task List with serializer
    """
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer


    
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    edit or delete single Tasks
    """
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer



class LoginView(ObtainAuthToken):
    """
    Login with Tokin view
    """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
class UserCreate(generics.CreateAPIView):
    """
    Create User Views
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    """
    Show registered User View with serializer
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class ContactList(generics.ListCreateAPIView):
    """
    Show Contact list  View with serializer
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactUpdate(generics.RetrieveUpdateDestroyAPIView):
    """
    View for update the Contacts
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer