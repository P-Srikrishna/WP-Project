"""Caduceus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('about', views.aboutus, name="About Us"),
    path('register', views.registration, name="Registration"),
    path('consult', views.consultation, name="Consultation"),
    path('counsel', views.counselling, name="Counselling"),
    path('nurse', views.nursing, name="Nursing"),
    path('eldercare', views.elder_care, name="Elder-Care"),
    path('covid', views.covid, name="COVID"),
]
