from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

def index(request):
    events = Event.objects.all()
    es = ", ".join([e.name and e.info for e in events])
    return HttpResponse(es)

def single(request, event_id):
    se = Event.objects.get(pk=event_id)
    ni = ", ".join([e.name and e.info for e in se])
    return HttpResponse(ni)

# def index(request):
#     return HttpResponse("testing testing, 1,2,3")
# # Create your views here.
