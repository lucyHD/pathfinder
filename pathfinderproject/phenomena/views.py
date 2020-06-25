from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Location

def index(request):
    #events = Event.objects.all()
    #es = ", ".join([e.name and e.info for e in events])  #ask neil to explain this
    all_events = {"events": Event.objects.all()}
    return render(request, "phenomena/index.html", all_events)
    #return HttpResponse(es)

def single(request, event_id):
    event = {"event": Event.objects.get(pk=event_id)}
    return render(request, "phenomena/single.html", event)

def locations(request):
    all_locations = {"locations": Location.objects.all()}
    return render(request, "phenomena/locations.html", all_locations)

def country(request, country):
    req_location = Location.objects.get(location=country)
    el = Event.objects.filter(location__location=req_location)
    return HttpResponse(el)

    

# def index(request):
#     return HttpResponse("testing testing, 1,2,3")
# # Create your views here.
