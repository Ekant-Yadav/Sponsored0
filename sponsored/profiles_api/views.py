from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import Sponsor, Organiser
from django.contrib.auth import login, logout, authenticate

def loginuser(request,slug):
    context={
        "slug":slug
    }
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        User= authenticate(username=username, password=password)
        login(request, User)
        if (User is not None):
            if Organiser.objects.filter(user=User).exists():
                return redirect("/organiser")
            elif Sponsor.objects.filter(user=User).exists():
                return redirect("/sponsor")
        else:
           return render(request, 'login.html')
    return render(request,'login.html',context)

def signupuser(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        email= request.POST.get('email')
        location= request.POST.get('location')
        profile = request.POST.get('profile')

        myuser=User.objects.create_user(username,email,password)
        myuser.set_password(password)
        myuser.save()
        
        if profile == "organiser":
            organiser = Organiser(user=myuser, location=location)
            organiser.save()
        if profile == "sponsor":
            sponsor = Sponsor(user=myuser, location=location)
            sponsor.save()    
        

        user= authenticate(username=username, password=password)
        login(request, user)
        return redirect("/organiser")
    return render(request,'signup.html')
