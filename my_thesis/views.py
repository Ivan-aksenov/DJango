from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.

def todos(request):
    data = TodoItem.objects.all()
    return render(request,"todos.html", {"todos": data})

def Home(request):
    return render(request, "my_thesis/Home.html")

def SignIn(request):
    return render(request,"my_thesis/SignIn.html")

def SignUp(request):
    return render(request,"my_thesis/SignUp.html")

def Features(request):
    return render(request, "my_thesis/Features.html")

def Insights(request):
    return render(request, "my_thesis/Insights.html")

def AboutUs(request):
    return render(request, "my_thesis/AboutUs.html")

def Contact(request):
    return render(request, "my_thesis/Contact.html")