from django.shortcuts import render
from django.http import HttpResponse
from .models import Film
from newsy.models import Newsy

# Create your views here.

def home(request):
    moje_filmy = Film.objects.all()
    return render(request, 'home.html', {'filmy': moje_filmy})

def about(request):
    return render(request, 'about.html')