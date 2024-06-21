
from django.db import models

class BusStop(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=100)
    bus_stops = models.ManyToManyField(BusStop, through='BusStopDestination')

    def __str__(self):
        return self.name

class BusStopDestination(models.Model):
    bus_stop = models.ForeignKey(BusStop, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('bus_stop', 'destination')

    def __str__(self):
        return f"{self.bus_stop.name} -> {self.destination.name}"
