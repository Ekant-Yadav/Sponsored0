from organiser import views
from django.urls import path


urlpatterns = [
   path("newevent",views.addevent,name="newevent"),
   path("event/<slug:slug>", views.event,name="event")
]