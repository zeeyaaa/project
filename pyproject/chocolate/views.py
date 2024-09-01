from django.shortcuts import render
from django.http import HttpResponse
from .models import Chocolate

def home(request):
    chocolate = Chocolate.objects.all()
    return render(request, 'home.html',{'chocolate': chocolate})

