from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import Sponsor, Organiser, City
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
    context = {'city': City.objects.all()}
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        email= request.POST.get('email')
        location= request.POST.get('location')
        profile = request.POST.get('profile')

        myuser=User.objects.create_user(username,email,password)
        myuser.set_password(password)
        myuser.save()
        
        city = City.objects.get(city=location)
        if profile == "organiser":
            organiser = Organiser(user=myuser)
            organiser.location = city
            organiser.save()
        if profile == "sponsor":
            sponsor = Sponsor(user=myuser)
            sponsor.location = city
            sponsor.save()    
        

        user= authenticate(username=username, password=password)
        login(request, user)
        goto = "/"+ profile
        return redirect(goto)
    return render(request,'signup.html',context)

def logoutuser(request):
    logout(request)
    return redirect("/")
