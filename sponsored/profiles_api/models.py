from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Organiser(models.Model):
    # Add city field to the User model

    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='+')
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class Sponsor(models.Model):
    # Add city field to the User model

    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='+')
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class City(models.Model):
    city = models.CharField(max_length=25)

    def __str__(self):
        return self.city

class Genere(models.Model):
    genere = models.CharField(max_length=25)

    def __str__(self):
        return self.genere

class Event(models.Model):
    title= models.CharField(max_length=30)

    city = models.ManyToManyField(City)
    genere = models.ManyToManyField(Genere)

    date= models.DateField()
    description= models.TextField()
    image= models.ImageField(height_field=None, width_field=None, max_length=None, null=True, blank=True)

    organiser= models.ForeignKey(Organiser, on_delete=models.CASCADE, null=True, blank=True)
    sponsor= models.ManyToManyField(Sponsor, null=True, blank=True)

    def __str__(self):
        return self.title

class SponsoredEvent(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE,related_name='+')

    def __str__(self):
        return self.event.title