from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.

def Home(request):
    return render(request, "Home.html")

def todos(request):
    data = TodoItem.objects.all()
    return render(request,"todos.html", {"todos": data})

def SignIn(request):
    return render(request,"SignIn.html")

def SignUp(request):
    return render(request,"SignUp.html")