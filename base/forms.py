from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django import forms


class AddHomeworkForm(ModelForm):
    class Meta:
        model = HomeWorkPost
        fields = ["assigned_to", "title", "subject", "text"]


class AddNotificationForm(ModelForm):
    class Meta:
        model = NotificationPost
        fields = ["assigned_to", "title", "text", "related_file"]


class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password", "profile_pic", "phone_number"]
