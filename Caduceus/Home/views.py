from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Registration1
from django.db import IntegrityError

# Create your views here.
def homepage(request):
    return render(request, "Homepage.html")

def aboutus(request):
    return render(request, "AboutUs.html")

def registration(request):

    if request.method == "POST":
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Address = request.POST.get('Address')
        PhoneNumber = request.POST.get('PhoneNumber')
        City = request.POST.get('City')
        Reg_object= Registration1(FirstName=FirstName, LastName=LastName,Email=Email,
        Password=Password,PhoneNumber=PhoneNumber,Address=Address,City=City, 
        date = datetime.today())
        Reg_object.save()
        
    return render(request, "registration.html")

def consultation(request):
    return render(request, "Services-info-Consultations.html")

def counselling(request):
    return render(request, "Services-info-Counselling.html")

def nursing(request):
    return render(request, "Services-info-Nursing.html")

def covid(request):
    return render(request, "Services-info-COVID.html")

def elder_care(request):
    return render(request, "Services-info-ElderCare.html")

def map(request):
    return render(request, "map.html", {})

