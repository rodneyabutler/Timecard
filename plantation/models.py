from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Plantation(models.Model):
    name = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    county = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    longitude = models.CharField(max_length=128)
    latitude = models.CharField(max_length=128)
    information = models.TextField(max_length=500)
    webpage = models.URLField(max_length=200) # for the URL of the plantation

class Route(models.Model):
    end_lat = models.CharField(max_length=120)
    end_long = models.CharField(max_length=120)

class Counties(models.Model):
    class Meta:
        verbose_name_plural = "counties"
    county_name = models.CharField(max_length=128)
    county_information = models.TextField(max_length=500)


class Location(models.Model):
    current_lat = models.CharField(max_length=120)
    current_long = models.CharField(max_length=120)

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
