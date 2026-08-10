from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name=("signup")),
    path("signin/", views.signin, name="signin"),
    path("tasks/", views.tasks, name="tasks"),
    path("tasks/create/", views.create_task, name="create_task"),
    path("logout/", views.signout, name="logout"),
]
