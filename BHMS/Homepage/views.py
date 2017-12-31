
from django.shortcuts import HttpResponse,render,redirect
from django.contrib.auth import authenticate
from .import views
from .models import userProfile
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from .forms import profileForm,commentForm

def Index(request):

    Context = {}
    print('Login fuction is called')
    a = userProfile.objects.all()
    for i in a:
        print(i.u_profile,"=",i.u_profile_id)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)

            for i in a:
                if user.id == i.u_profile_id:
                    print('the fuck you this is true')

            return HttpResponse('Congratulations you are logged in.' + username +str(user.id))
        else:
            return HttpResponse('You have entered wrong password')





    return render(request,'Homepage/index.html',Context)

def user_register(request):
    form = commentForm()
    form1 = profileForm()
    # formb = commentForm()




    Context = {
        'form': form,
        'form1': form1
    }
    return render(request,'Homepage/register.html',Context)

def my_cv(request):
    return render(request,'Homepage/my_cv.html',{})
