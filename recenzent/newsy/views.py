from django.shortcuts import render
from .models import Newsy

# Create your views here.

def newsy(request):
    moje_newsy = Newsy.objects.all()
    return render(request, 'newsy.html', {'newsy': moje_newsy})


def newsy_detail(request, news_id):
    moje_newsy = Newsy.objects.get(id=news_id)
    return render(request, 'newsy/newsy_detail.html', {'news': moje_newsy})
