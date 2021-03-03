from django.urls import path
from . import views

app_name = 'sponsor'

urlpatterns = [
    path('sponsored', views.SponsoredEvents.as_view(), name='sponsored_events'),
    path('event/<int:pk>', views.EventDetails.as_view(), name='event_detail'),
    path('add-sponsor/<int:pk>', views.add_sponsor, name='add_sponsor'),
    path('<int:pk>', views.CityEvents.as_view(), name='homepage'),
    path('', views.NearByEvents.as_view(), name='city_list')
]