from django.db import models

# Create your models here.

<<<<<<< Updated upstream
=======
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
>>>>>>> Stashed changes

# class User():
#     user_id = models.ForeignKey(on_delete=models.CASCADE)
#     user_name = models.CharField(max_length=200)
#     user_type = models.TextChoices()

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
<<<<<<< Updated upstream
    created_at = models.DateField(auto_created=True)
=======
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
>>>>>>> Stashed changes
