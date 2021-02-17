from django.shortcuts import render, redirect
from profiles_api.models import Sponsor, Event, City, Genere, SponsoredEvent
from django.views import View
from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.
# def event(request, pk):
    # city = request.user.city
    # event = Event.objects.get(pk=pk)
    # request.session['pk'] = pk


    # if SponsoredEvent.objects.get(event=event).exists():
    #     advertised="YES"
    # else:
    #     advertised="NO"

    # context={
    #     'title':event.title,
    #     'city':City.objects.filter(event=event),
    #     'genere':Genere.objects.filter(event=event),
    #     'date':event.date,
    #     'description':event.description,
    #     'advertised':advertised,
    #     'sponsor':Sponsor.objects.filter(event=event),
    #     'addSponsor': reverse_lazy('add_sponsor')
    # }
    # return render(request,
    #             "eventDetailSponsor.html",
    #             context
    # )

class EventDetails(DetailView):
    model = Event
    template_name = "eventDetailSponsor.html"
    context_object_name = 'event'

    def get_queryset(self):
        event = Event.objects.filter(pk=self.kwargs["pk"])
        return event
    

    # def get_context_data(self, **kwargs):

    #     pk = self.kwargs['pk']
    #     print(pk)
    #     event = self.model.objects.get(pk=pk)

    #     if SponsoredEvent.objects.get(event=event).exists():
    #         advertised="YES"
    #     else:
    #         advertised="NO"

    #     context = super(Event, self).get_context_data(**kwargs)
    #     context['advertised'] = advertised
    #     return context

class AddSponsor(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['sponsor']
    template_name = 'add_sponsor.html'

    def get_success_url(self):
        # url = super(AddSponsor, self).get_success_url()
        url = reverse('event_detail', kwargs={'pk':self.kwargs['pk']})
        return url

# def add_sponsor(request, pk):
#     event = get_object_or_404(Event, pk=pk)
#     user = request.user

#     if request.user.is_anonymous or not(Sponsor.objects.filter(user=user).exists()):
#         return redirect('/')

#     else:
#         sponsor = Sponsor.objects.get(user=user)
#         if 'sponsor' in request.POST:
#             if 'add_sponsor' == request.POST.get('sponsor'):
#                 event.sponsor = sponsor
#             return redirect(reverse('event_detail'), kwargs={'pk':pk})
#         return redirect(reverse('add_sponsor', kwargs={'pk':pk}))

class NearByEvents(LoginRequiredMixin, ListView):

    model = Event
    template_name = "sponsor.html"
    context_object_name = 'events'

    def get_queryset(self):
        city = City.objects.get(pk=self.kwargs["pk"])
        return Event.objects.filter(city=city)


class CityList(ListView):

    model = City
    template_name = "city.html"
    context_object_name = 'citys'