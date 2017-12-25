
from django.shortcuts import HttpResponse,render,redirect
from django.contrib.auth import authenticate
from .forms import Nameform
from .import views
from django.contrib.auth import login,logout
from django.contrib.auth.models import User

def Index(request):



    form = Nameform()

    Context = {
        'form':form,

    }
    print('Login fuction is called')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            print(username, password)

            return render(request, 'Homepage/index.html',Context)
        else:
            return HttpResponse('You have entered wrong password')





    return render(request,'Homepage/index.html',Context)

def user_register(request):
    Context = {

    }
    return render(request,'Homepage/register.html',Context)
