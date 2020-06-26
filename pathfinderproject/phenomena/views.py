from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Location, Date

def index(request):
    #events = Event.objects.all()
    #es = ", ".join([e.name and e.info for e in events])  #ask neil to explain this
    all_events = {"events": Event.objects.all()}
    return render(request, "phenomena/index.html", all_events)
    #return HttpResponse(es)

def single(request, event_id):
    event = {"event": Event.objects.get(pk=event_id)}
    # date = {"date": Date.objects.get(pk=event_id)}
    return render(request, "phenomena/single.html", event)

def locations(request):
    all_locations = {"locations": Location.objects.all()}
    return render(request, "phenomena/locations.html", all_locations)

def country(request, country):
    req_location = Location.objects.get(location=country)
    event_location = {"events": Event.objects.filter(location__location=req_location)}
    return render(request, "phenomena/country.html", event_location)

def dates(request):
    all_dates = {"dates": Date.objects.all()}
    return render(request, "phenomena/dates.html", all_dates)


# def specificdate (request, specificdate):
#     req_date = Date.objects.get(date=specificdate)
#     event_date = {"dates": Date.objects.filter(date__date=req_date)}
#     return render(request, "phenomena/specificdate.html", event_date)





    

# def index(request):
#     return HttpResponse("testing testing, 1,2,3")
# # Create your views here.


#remember when changing from http response to render, it needs to be a dictionary
