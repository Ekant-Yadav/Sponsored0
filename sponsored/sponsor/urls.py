from django.urls import path
from . import views

app_name = 'sponsor'

urlpatterns = [
    # function based views
    # path('addsponsor/<int:pk>/', views.add_sponsor, name='add_sponsor'),

    # class based views
    path('event/<int:pk>/', views.EventDetails.as_view(), name='event_detail'),
    path('<int:pk>/', views.NearByEvents.as_view(), name='homepage'),
    path('', views.CityList.as_view(), name='city_list'),
    path('addsponsor/<int:pk>', views.AddSponsor.as_view(), name='add_sponsor')
]