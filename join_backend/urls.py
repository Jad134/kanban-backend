"""
URL configuration for join_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from taskapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', views.TaskListCreate.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('login/', views.LoginView.as_view()),
    path('register/', views.UserCreate.as_view(), name='user-register'),
    path('users/', views.UserList.as_view()), 
    path('contact/', views.ContactList.as_view()),
    path('contact/<int:pk>/', views.ContactUpdate.as_view()), 
]
