from django.forms import ModelForm
from profiles_api.models import Event,Genere
from django import forms

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ("title","city","genere","date","description","image")
        widgets={
        'genere': forms.CheckboxSelectMultiple(),
        'city': forms.CheckboxSelectMultiple(),
        }
    
