from razv4_0.models import Razvozka
from django.shortcuts import render
from datetime import datetime


def print_all(request, date_rzv):
    razvozki = Razvozka.objects.filter(date=datetime.strptime(date_rzv, '%Y-%m-%d').date())
    context = {'razvozki': razvozki}
    return render(request, 'print.html', context)


def print_one(request, date_rzv, driver_id):
    razvozki = Razvozka.objects.filter(date=datetime.strptime(date_rzv, '%Y-%m-%d').date(), driver__id=driver_id)
    context = {'razvozki', razvozki}
    return render(request, 'print.html', context)
