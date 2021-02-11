from django.contrib import admin
from .models import Sponsor, Organiser,City,Genere,Event,SponsoredEvent

admin.site.register(Sponsor)
admin.site.register(Organiser)
admin.site.register(City)
admin.site.register(Genere)
admin.site.register(Event)
admin.site.register(SponsoredEvent)
