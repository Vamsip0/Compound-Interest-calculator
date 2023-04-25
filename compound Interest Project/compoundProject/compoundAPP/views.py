from django.shortcuts import render
import requests


def compoundInterest(request):
    rate=None
    if request.method=="POST":
        amount=float(request.POST["amount"])
        time=float(request.POST["time"])
        rate=float(request.POST['rate'])
        interest=amount * (1+rate/100)**time
        interest=round(interest,2)
        
    return render(request, 'index.html', {'interest': interest})