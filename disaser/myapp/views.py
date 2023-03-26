from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import *
from myapp.models import*
# Create your views here.

def index(request):
    return render(request,'myhomepage.html')

def log(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            request.session['username'] = username
            return render(request,'offreg.html',{"user":user})
        else:
            return HttpResponse("INVALID CREDENTIALS")
    else:
        return render(request, 'home.html')