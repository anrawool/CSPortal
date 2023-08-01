from django.shortcuts import render, redirect

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import *

# from .models import User
import datetime
from . import models

# from plyer import notification

# Create your views here.

User = get_user_model()


@login_required(login_url="login")
def HomeView(request):
    assigned_homeworks = models.HomeWorkPost.objects.filter(assigned_to=request.user)
    assigned_notifications = models.NotificationPost.objects.filter(
        assigned_to=request.user
    )
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    day_index = datetime.date.today().weekday()
    context = {
        "assigned_homeworks": assigned_homeworks,
        "assigned_notifications": assigned_notifications,
        "today_date": datetime.date.today().strftime("%d/%m"),
        "today_day": days[day_index],
        "user": request.user,
    }
    return render(request, "base/index.html", context)  # Home Page View


def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Credentials")

    context = {"page": page}
    return render(request, "base/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("home")


def registerUser(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email
            user.save()
            login(request, user)
            return redirect("home")
        else:
            all_errors = []
            for field, errors in form.errors.items():
                all_errors.extend(errors)
            for error in all_errors:
                messages.error(request, error)
            context = {"formvals": request.POST}
            return render(request, "base/login_register.html", context)
    return render(request, "base/login_register.html", {"form": form})


@login_required(login_url="login")
def HomeworkPage(request):
    all_homeworks = models.HomeWorkPost.objects.filter(assigned_to=request.user)
    context = {"all_homeworks": all_homeworks}
    return render(request, "base/homeworks.html", context=context)


@login_required(login_url="login")
def NotificationPage(request):
    all_notifications = models.NotificationPost.objects.filter(assigned_to=request.user)
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    day_index = datetime.date.today().weekday()
    context = {
        "all_notifications": all_notifications,
        "today_date": datetime.date.today().strftime("%d/%m"),
        "today_day": days[day_index],
    }
    return render(request, "base/notifications.html", context=context)


# Try to integrate like signup or login
@login_required(login_url="login")
def AddHomework(request):
    form = AddHomeworkForm()
    if request.method == "POST":
        form = AddHomeworkForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.assigned_by = request.user
            form.save()
            form.save_m2m()
            # notification.notify(title = "New Homework", message=f"{form.title}" ,timeout=1)
            return redirect("home")
        else:
            all_errors = []
            print(form.errors)
            for field, errors in form.errors.items():
                all_errors.extend(errors)
            print(all_errors)
            if "This field is required." in all_errors:
                all_errors = ["All Fields Are Required"]
            for error in all_errors:
                messages.error(request, error)
            context = {"formvals": request.POST, "users": models.User.objects.all()}
            return render(request, "base/add_homework.html", context)

    context = {"form": form, "users": models.User.objects.all()}
    return render(request, "base/add_homework.html", context)


@login_required(login_url="login")
def AddNotification(request):
    form = AddNotificationForm()
    if request.method == "POST":
        form = AddNotificationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.assigned_by = request.user
            form.save()
            form.save_m2m()
            return redirect("home")
        else:
            all_errors = []
            print(form.errors)
            for field, errors in form.errors.items():
                all_errors.extend(errors)
            if "This field is required." in all_errors:
                all_errors = ["All Fields Are Required"]
            for error in all_errors:
                messages.error(request, error)
            context = {"formvals": request.POST, "users": models.User.objects.all()}
            return render(request, "base/add_notification.html", context)

    context = {"form": form, "users": models.User.objects.all()}
    return render(request, "base/add_notification.html", context)
