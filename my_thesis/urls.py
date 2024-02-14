from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("todos/", views.todos, name="Todos"),
    path("SignIn/", views.SignIn, name="SignIn"),
    path("SignUp/", views.SignUp, name="SignUp"),
    path("Features_Insights/", views.Features_Insights, name="Features_Insights"),
    path("AboutUs_Contact/", views.AboutUs_Contact, name="AboutUs_Contact"),
    path("Client_Dash/", views.Client_Dash, name="Client_Dash"),
]