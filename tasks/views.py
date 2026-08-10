from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from .form import TaskForm


def home(request):
    return render(request, "home.html")


# Create your views here.


def signup(request):

    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})

    elif request.method == "POST":
        # print(request.POST)

        try:
            if request.POST["password1"] == request.POST["password2"]:
                # register user
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("tasks")
                return HttpResponse("User created successfully")

            else:
                return render(
                    request,
                    "signup.html",
                    {"form": UserCreationForm, "error": "password do not match"},
                )

        except IntegrityError as e:
            print(e)
            return render(
                request,
                "signup.html",
                {"form": UserCreationForm, "error": "username already exists"},
            )

    else:
        print("metodo no autorizado")


def signin(request):

    if request.method == "GET":

        return render(request, "signin.html", {"form": AuthenticationForm()})
    elif request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )

        if user is None:
            return render(
                request,
                "signin.html",
                {
                    "form": AuthenticationForm,
                    "error": "Username or password is incorrect",
                },
            )
        else:
            login(request, user)
            return redirect("home")

    else:
        return HttpResponse("<h1> Metodo no permitido</h1>")


def signout(request):
    logout(request)
    return redirect("home")


def tasks(request):
    return render(request, "tasks.html")


def create_task(request):

    if request.method == "GET":
        return render(request, "create_task.html", {"form": TaskForm()})
    elif request.method == "POST":
        try:

            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("tasks")
        except ValueError as e:
            print(e)
            return render(
                request,
                "create_task.html",
                {"form": TaskForm(), "error": "Please provide valida data"},
            )
    else:
        return HttpResponse("<h1>Metodo no permitido</h1>")
