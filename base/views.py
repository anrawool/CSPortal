from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from . import models
# Create your views here.

@login_required(login_url='login')
def HomeView(request):
    return render(request, 'base/index.html') # Home Page View

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials") 

    context = {"page":page}
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
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            all_errors = []
            for field, errors in form.errors.items():
                all_errors.extend(errors)
            for error in all_errors:
                messages.error(request, error) 
            context = {"formvals": request.POST}
            return render(request, 'base/login_register.html', context)
    return render(request, 'base/login_register.html', {"form":form})


@login_required(login_url='login')
def HomeworkPage(request):
    all_homeworks = models.HomeWorkPost.objects.all()
    context = {"all_homeworks": all_homeworks}
    return render(request, "base/homeworks.html", context=context)