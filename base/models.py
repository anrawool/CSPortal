from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"

    base_role = Role.STUDENT

    username = models.CharField(max_length=200, unique=True, default="Guest", null=True)
    email = models.EmailField(max_length=200, unique=True, editable=True)
    phone_number = models.IntegerField(null=True, editable=True)
    emergency_number = models.IntegerField(null=True, editable=True, default=0000000000)
    profile_pic = models.ImageField(
        null=True,
        blank=True,
        upload_to="./uploads/profile_pics",
        default="./uploads/profile_pics/default_male_avatar.svg",
    )
    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone_number"]

    objects = UserManager()
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Student(User):
    base_role = User.Role.STUDENT

    objects = StudentManager()

    class Meta:
        proxy = True


class Teacher(User):
    base_role = User.Role.TEACHER
    objects = TeacherManager()

    class Meta:
        proxy = True


class HomeWorkPost(models.Model):
    assigned_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assigned_by", null=True
    )
    assigned_to = models.ManyToManyField(User, related_name="assigned_to")
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, default="General")
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]


class NotificationPost(models.Model):
    assigned_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="given_by", null=True
    )
    assigned_to = models.ManyToManyField(User, related_name="give_to")
    title = models.CharField(max_length=200)
    text = models.TextField()
    related_file = models.FileField(upload_to="./uploads", null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admission_number = models.IntegerField(null=True, blank=True, unique=True)
    grade = models.IntegerField(null=True)
    roll_number = models.IntegerField(null=True)
    father_name = models.CharField(max_length=200, editable=False, null=True) 
    mother_name = models.CharField(max_length=200, editable=False, null=True) 

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STUDENT":
        StudentProfile.objects.create(user=instance)