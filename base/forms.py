from django.forms import ModelForm
from .models import *

class AddHomeworkForm(ModelForm):
    class Meta:
        model = HomeWorkPost
        fields = ['assigned_to', 'title', 'subject', 'text']

class AddNotificationForm(ModelForm):
    class Meta:
        model = NotificationPost
        fields = ['assigned_to', 'title', 'text', 'related_file']