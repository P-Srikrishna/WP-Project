from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return render(request, "Homepage.html")

def aboutus(request):
    return HttpResponse("This page is About Us")

def registration(request):
    return HttpResponse("This page is for you to register")

def consultation(request):
    return HttpResponse("This is our Consultation page")

def counselling(request):
    return HttpResponse("This is our wise Counsel page")

def nursing(request):
    return HttpResponse("This page is for our nurses")

def covid(request):
    return HttpResponse("we're ready to help you, please help youself")

def elder_care(request):
    return HttpResponse("This page is for our elders along with our care")

