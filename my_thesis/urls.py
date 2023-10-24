from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("todos/", views.todos, name="Todos"),
    path("SignIn/", views.SignIn, name="SignIn"),
    path("SignUp/", views.SignUp, name="SignUp")
]