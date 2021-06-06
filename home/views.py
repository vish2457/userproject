from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from home.models import Booking
from collections import defaultdict
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')


def payment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Address= request.POST.get('Address')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        age = request.POST.get('age')
        aadhar_no = request.POST.get('aadhar_no')
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        Seat = request.POST.get('Seat')
        booking = Booking(name=name, Address=Address , email=email, mobile_no=mobile_no, age=age, aadhar_no=aadhar_no, source=source, destination=destination, Seat=Seat)
        booking.save()
        messages.success(request, "Successfully Booked the Ticket")
    return render(request, 'payment.html')


def Order_History(request):
    objs = Booking.objects.all()
    amount = defaultdict(int)
    for obj in objs:
        if obj.source == "Hubli" :
            amount[obj.id] = 3000
        elif obj.source == "Bangalore" :
            amount[obj.id] = 4000
        elif obj.source == "Mumbai" :
            amount[obj.id] = 3500
        elif obj.source == "Delhi" :
            amount[obj.id] = 5000
        elif obj.source == "Chennai" :
            amount[obj.id] = 3700
        elif obj.source == "Kolkata" :
            amount[obj.id] = 4200
        elif obj.source == "Pune":
            amount[obj.id] = 3999
        elif obj.source == "Lucknow":
            amount[obj.id] = 3200
        elif obj.source == "Shimla":
            amount[obj.id] = 4500


    context = {
       "object_list": objs, "amt": amount.items()
    }
    return render(request, "display.html", context)

def cancel_ticket(request):
    objs = Booking.objects.all()
    context = {
        "object_list": objs
    }
    if request.method == "POST":
        aadhar_no = request.POST.get('aadhar_no')
        record = objs.get(aadhar_no=aadhar_no)
        record.delete()
        return HttpResponseRedirect("/")

    return render(request, "delete.html", context)