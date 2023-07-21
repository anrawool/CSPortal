from django.db import models

# Create your models here.


# class User():
#     user_id = models.ForeignKey(on_delete=models.CASCADE)
#     user_name = models.CharField(max_length=200)
#     user_type = models.TextChoices()


class HomeWorkPost(models.Model):
    # post_id = models.ForeignKey(on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    # subject = models.TextChoices()
    text = models.TextField()
    created_at = models.DateField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

class NotificationPost(models.Model):
    # post_id = models.ForeignKey(on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateField(auto_created=True)
