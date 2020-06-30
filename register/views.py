from django.shortcuts import render, redirect
from .forms import RegisterForm
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# @csrf_exempt
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid:
            form.save()
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})
