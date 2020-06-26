from django.urls import path
from . import views

urlpatterns = [

    path("<int:event_id>/", views.single, name="single"),
    path("", views.index, name="index"),
    path("locations/", views.locations, name="locations"),
    path("country/<str:country>/", views.country, name="country"),
    path("dates/", views.dates, name="dates")
] 


# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# urlpatterns += staticfiles_urlpatterns()



#index path is phenomena/ (with nothing else). We specified this in urls.py(pathfinderproject). index is the name we give it, and the function that fires in views.py in response to a user going to that URL.
#single path is the id number of the event after phenomena (phenomena/5/)

#we bind the views.index function to "" and give it the name "index"
#we can then use the name index as a template
#remember, single is just the name we are giving it(we can also use this to link in the html) and it relates to the function single in views. The address the user is entering is phenomena/5 (or another number that is an event id)

#can add path converters. Above is int and str. Anything in <> captures that value (so you can then use it in the function)