from django.contrib import admin
from .models import Contact, Profile, TaskModel
# Register your models here.
admin.site.register(TaskModel)
admin.site.register(Profile)
admin.site.register(Contact)
