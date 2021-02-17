from django.urls import path
from . import views

app_name = 'sponsor'

urlpatterns = [
    path('event/<int:pk>', views.EventDetails.as_view(), name='event_detail'),
    path('add-sponsor/<int:pk>', views.add_sponsor, name='add_sponsor'),
    path('<slug:slug>', views.NearByEvents.as_view(), name='homepage'),
    path('', views.CityList.as_view(), name='city_list')
]