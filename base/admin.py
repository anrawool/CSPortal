from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = models.StudentProfile
    can_delete = False

class StudentProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]


admin.site.register(models.HomeWorkPost)
admin.site.register(models.User, StudentProfileAdmin)
admin.site.register(models.StudentProfile)
admin.site.register(models.NotificationPost)
