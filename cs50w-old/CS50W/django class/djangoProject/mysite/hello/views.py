from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Flight,Passenger
from django.urls import reverse

# Create your views here.

def index(request):
    context={
        "flights": Flight.objects.all()
    }
    return render(request, "hello/index.html", context)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id) #here pk = id
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")
    context = {
        "flight":flight,
        "passengers":flight.passengers.all(),
        "non_passengers":Passenger.objects.exclude(flights=flight).all()
    }
    return render(request, "hello/flight.html", context)

def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request,"hello/error.html",{"message":"No Selection"})
    except Flight.DoesNotExist:
        return render(request, "hello/error.html",{"message":"Flight does not exist"})
    except Passenger.DoesNotExist:
        return render(request, "hello/error.html",{"message":"Passenger does not exist"})
    
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))# reverse of going from name of url to actual url, args need to be iterable by adding ,



