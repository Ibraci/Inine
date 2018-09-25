from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

class Plug(models.Model):
    name = models.CharField(max_length=80)
    status = models.BooleanField(default=False)
    port = models.IntegerField(unique=True)
    room = models.ManyToManyField(Room)
    created_at = models.DateTimeField(auto_now_add=True)

class Bulb(models.Model):
    name = models.CharField(max_length=80)
    status = models.BooleanField(default=False)
    connect = models.BooleanField(default=True)
    port = models.IntegerField(unique=True)
    port_connect = models.IntegerField(default=0)
    room = models.ManyToManyField(Room)
    created_at = models.DateTimeField(auto_now_add=True)
