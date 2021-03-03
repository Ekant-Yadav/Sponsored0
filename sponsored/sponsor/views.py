from django.shortcuts import render, redirect
from profiles_api.models import Sponsor, Event, City, Genere, SponsoredEvent, Organiser
from django.views import View
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

class EventDetails(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "eventDetailSponsor.html"
    context_object_name = 'event'
    


def add_sponsor(request, pk):
    event = get_object_or_404(Event, pk=pk)
    user = request.user
    organiser = Organiser.objects.get(event=event)

    

    if request.user.is_anonymous or not(Sponsor.objects.filter(user=user).exists()):
        return redirect('/')

    else:
        sponsor = Sponsor.objects.get(user=user)
        receiver = organiser.user.email
        email = EmailMessage(
            'Someone wants to sponsor your event',
            'Hey, ',
            settings.EMAIL_HOST_USER,
            [receiver]
        )
        email.fail_silently=False
        email.send()
        if 'sponsor' in request.POST:
            if 'add_sponsor' == request.POST.get('sponsor'):
                event.sponsor = sponsor
                
            return redirect("/sponsor")
        return redirect('/sponsor')


class CityEvents(LoginRequiredMixin, ListView):

    model = Event
    template_name = "sponsor.html"
    context_object_name = 'events'

    def get_queryset(self):
        city = City.objects.get(pk=self.kwargs["pk"])
        return Event.objects.filter(city=city)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CityEvents, self).get_context_data(**kwargs)
        context['city'] = City.objects.get(pk=self.kwargs["pk"])
        return context

class NearByEvents(LoginRequiredMixin, ListView):

    model = City
    template_name = "city.html"
    context_object_name = 'citys'

    def get_context_data(self, *, object_list=None, **kwargs):
        sponsor = Sponsor.objects.get(user=self.request.user)
        city = sponsor.location
        context = super(NearByEvents, self).get_context_data(**kwargs)
        context['near_events'] = Event.objects.filter(city=city)
        return context

class SponsoredEvents(LoginRequiredMixin, ListView):
    
    template_name = 'sponsored_events.html'
    context_object_name = 'events'
    

    def get_queryset(self):
        sponsor = Sponsor.objects.get(user=self.request.user)
        return Event.objects.filter(sponsor=sponsor)