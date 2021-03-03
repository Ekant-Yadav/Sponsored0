from organiser import views
from django.urls import path


urlpatterns = [
   path("newevent",views.addevent,name="newevent"),
   path("event/<str:slug>", views.event,name="event")
]