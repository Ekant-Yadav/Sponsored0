from django.shortcuts import render, redirect
from profiles_api.models import Sponsor, Event, City, Genere, Organiser
from django.views import View
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def event_detail(request, pk):
    user = request.user
    if request.user.is_anonymous or not(Sponsor.objects.filter(user=user).exists()):
         return redirect('/')

    else:
        event = get_object_or_404(Event, pk=pk)
        organiser = Organiser.objects.get(event=event)

        context={
            'event':event,
            'title':'Event'
        }

        if request.method == "POST":
            sponsor = Sponsor.objects.get(user=user)
            event.sponsor.add(sponsor)
            receiver = organiser.user.email
            message = request.POST.get('msg')
            template = render_to_string('email_template.html', {'sponsor': user.username, 'event': event.title, 'mail': user.email, 'message':message})
            email = EmailMessage(
                'Someone wants to sponsor your event',
                template,
                settings.EMAIL_HOST_USER,
                [receiver]
            )
            email.fail_silently=False
            email.send()
            return redirect("/sponsor/sponsored")

        return render(request,"eventDetailSponsor.html", context)

    




class CityEvents(LoginRequiredMixin, ListView):

    model = Event
    template_name = "sponsor.html"
    context_object_name = 'events'

    def get_queryset(self):
        sponsor = Sponsor.objects.get(user=self.request.user)
        city = City.objects.get(pk=self.kwargs["pk"])
        return Event.objects.filter(city=city, advertised = True)

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
        context['near_events'] = Event.objects.filter(city=city, advertised = True)
        return context

class SponsoredEvents(LoginRequiredMixin, ListView):
    
    template_name = 'sponsored_events.html'
    context_object_name = 'events'
    

    def get_queryset(self):
        sponsor = Sponsor.objects.get(user=self.request.user)
        return Event.objects.filter(sponsor=sponsor)