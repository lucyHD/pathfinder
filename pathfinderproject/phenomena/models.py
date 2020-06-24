from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=750)

    def __str__(self):
        return self.name
    

class Date(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField(null=True)

    def __str__(self):
        return str(self.date) 

    
class Location(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location



# Create your models here.

