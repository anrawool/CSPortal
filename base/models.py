from django.db import models

# Create your models here.


# class User():
#     user_id = models.ForeignKey(on_delete=models.CASCADE)
#     user_name = models.CharField(max_length=200)
#     user_type = models.TextChoices()


class HomeWorkPost(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, default="General")
    text = models.TextField()
    created_at = models.DateField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    # completed = models.CharField(max_length=5, choices=[('Yes', 'Completed'), ('No', 'Not-Completed')], default="Not-Completed")

    class Meta:
        ordering = ['-created_at', '-updated_at']


class NotificationPost(models.Model):
    # post_id = models.ForeignKey(on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateField(auto_created=True)
