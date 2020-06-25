from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Location

def index(request):
    events = Event.objects.all()
    es = ", ".join([e.name and e.info for e in events])  #ask neil to explain this 
    return HttpResponse(es)

def single(request, event_id):
    events = Event.objects.get(pk=event_id)
    es = ", ".join([e.name for e in events])
    return HttpResponse(es)

def locations(request):
    locations = Location.objects.all()
    ls = ", ".join([l.location for l in locations])
    return HttpResponse(ls)

def country(request, country):
    req_location = Location.objects.filter(location=country)
    el = Event.objects.filter(location__location=req_location)


    # ev = Event.objects.all().filter(location=req_location)
    return HttpResponse(el)

    

# def index(request):
#     return HttpResponse("testing testing, 1,2,3")
# # Create your views here.
