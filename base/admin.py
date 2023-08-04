from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.

<<<<<<< HEAD
<<<<<<< Updated upstream
admin.site.register(models.HomeWorkPost)
=======
=======
>>>>>>> 82cee63125e74583a843f51089f1bada108128f6
class UserProfileInline(admin.StackedInline):
    model = models.StudentProfile
    can_delete = False

class StudentProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]


admin.site.register(models.HomeWorkPost)
admin.site.register(models.User, StudentProfileAdmin)
admin.site.register(models.StudentProfile)
admin.site.register(models.NotificationPost)
<<<<<<< HEAD
>>>>>>> Stashed changes
=======
>>>>>>> 82cee63125e74583a843f51089f1bada108128f6
