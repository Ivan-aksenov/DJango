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

def Features_Insights(request):
    return render(request, "my_thesis/Features_Insights.html")

def AboutUs_Contact(request):
    return render(request, "my_thesis/AboutUs_Contact.html")