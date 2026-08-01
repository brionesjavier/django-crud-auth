from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse


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
                return HttpResponse("User created successfully")

            else:
                return render(
                    request,
                    "signup.html",
                    {"form": UserCreationForm,
                     "error": "password do not match"},
                )

        except IntegrityError as e:
            print(e)
            return render(
                request,
                "signup.html",
                {"form": UserCreationForm,
                 "error": "username already exists"},
            )

    else:
        print("metodo no autorizado")
