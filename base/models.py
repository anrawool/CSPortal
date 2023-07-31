from django.db import models
from django.contrib.auth.models import User

class HomeWorkPost(models.Model):
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_by", null=True)
    assigned_to = models.ManyToManyField(User, related_name="assigned_to")
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, default="General")
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']


class NotificationPost(models.Model):
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_by', null=True)
    assigned_to = models.ManyToManyField(User, related_name='give_to')
    title = models.CharField(max_length=200)
    text = models.TextField()
    related_file = models.FileField(upload_to='../media/uploads', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']
