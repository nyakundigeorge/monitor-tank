from __future__ import unicode_literals
from django.db import models
from core.models import Base


class Subscriber(Base):
    subscriber_number = models.CharField(unique=True, max_length=11)
    access_token = models.CharField(max_length=100)
    name = models.CharField(max_length=20, blank=True, default="")
    address = models.CharField(max_length=50, blank=True, default="")
    role = models.CharField(max_length=50, blank=True, default="")


class Report(Base):
    context = models.TextField(max_length=300)
    pH_level = models.FloatField(max_length=10, default=0)
    oxygen_level = models.FloatField(max_length=10, default=0)
    temperature_level = models.FloatField(max_length=10, default=0)
    water_level = models.CharField(max_length=20, null=True, blank=True)
    fish_number = models.IntegerField(null=True, blank=True)
    average_fishes_weight = models.FloatField(max_length=5, null=True, blank=True)
    fish_feed_grams = models.FloatField(null=True, blank=True)
    feed_number = models.IntegerField(null=True, blank=True)
    feeder_grams = models.FloatField(null=True, blank=True)
