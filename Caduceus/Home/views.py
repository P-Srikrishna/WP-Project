from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return render(request, "Homepage.html")

def aboutus(request):
    return render(request, "AboutUs.html")

def registration(request):
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

