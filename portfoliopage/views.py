from django.shortcuts import render
from django.http import HttpResponse
from .models import TravelingPost

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def snowboarding(request):
    return render(request, 'snowboarding.html')

def traveling(request):
    travelPostObj = TravelingPost.objects.all()
    context = { 'posts': travelPostObj}
    return render(request, 'traveling.html', context)
