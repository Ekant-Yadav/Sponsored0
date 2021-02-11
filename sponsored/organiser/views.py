from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from profiles_api.models import Organiser,Event,City,Genere,Organiser,Sponsor,SponsoredEvent
from .forms import EventForm

def events(request):
    myuser= request.user
    if request.user.is_anonymous or not(Organiser.objects.filter(user=myuser).exists()):
        return redirect('/')
    else:
        org = Organiser.objects.get(user=myuser)
        context={
            'title': Event.objects.filter(organiser=org)
        }
        return render(request,'organiser.html',context)


def addevent(request):
    myuser= request.user
    if request.user.is_anonymous or not(Organiser.objects.filter(user=myuser).exists()):
        return redirect('/')
    else:
        form = EventForm()
        context={'form':form}
        if request.method == "POST":
            org = Organiser.objects.get(user=myuser)
            organiser= Event(organiser=org)
            form= EventForm(request.POST, instance=organiser)
            if form.is_valid():
                form.save()
            return redirect('/organiser')
        return render(request,'newevent.html',context)

def event(request, slug):
    myuser= request.user
    if request.user.is_anonymous or not(Organiser.objects.filter(user=myuser).exists()):
        return redirect('/')
    else:
        org = Organiser.objects.get(user=myuser)
        evenT= Event.objects.get(title=slug, organiser=org)
        if SponsoredEvent.objects.filter(event=evenT).exists():
            advertised="YES"
        else:
            advertised="NO"
        context={
            'title':evenT.title,
            'city':City.objects.filter(event=evenT),
            'genere':Genere.objects.filter(event=evenT),
            'date':evenT.date,
            'description':evenT.description,
            'advertised':advertised,
            'sponsor':Sponsor.objects.filter(event=evenT)
        }
        if request.method=="POST":
            if not(SponsoredEvent.objects.filter(event=evenT).exists()):
                sponsoredevent= SponsoredEvent(event=evenT)
                sponsoredevent.save()
            return redirect('/event/'+evenT.title)
        return render(request,'event.html',context)
