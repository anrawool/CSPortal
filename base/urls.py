from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.HomeView, name="home"),
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerUser, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path("homeworks/", views.HomeworkPage, name="homeworks"),
    path("notifications/", views.NotificationPage, name="notifications"),
    path("add_homework/", views.AddHomework, name="add-homework"),
    path("add_notification/", views.AddNotification, name="add-notification"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
