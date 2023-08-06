from razv4_0.models import Razvozka, Driver
from django.shortcuts import render
from datetime import datetime


def print_all(request, date_rzv):
    razvozki = Razvozka.objects.filter(date=datetime.strptime(date_rzv, '%Y-%m-%d').date(), deleted=False)
    drivers = Driver.objects.filter(deleted=False)
    context = {'razvozki': razvozki, 'drivers': drivers}
    return render(request, 'print.html', context)


def print_one(request, date_rzv, driver_id):
    drivers = Driver.objects.filter(deleted=False,
                                    razvozka__date=datetime.strptime(date_rzv, '%Y-%m-%d').date()).distinct()
    if driver_id != 0:
        razvozki = Razvozka.objects.filter(date=datetime.strptime(date_rzv, '%Y-%m-%d').date(), driver__id=driver_id,
                                           deleted=False)
        driver = Driver.objects.get(deleted=False, id=driver_id)
    else:
        razvozki = Razvozka.objects.filter(date=datetime.strptime(date_rzv, '%Y-%m-%d').date(), deleted=False)
        driver = ''

    context = {'razvozki': razvozki, 'drivers': drivers, 'driver': driver, 'date_rzv': date_rzv, 'driver_id': driver_id}
    return render(request, 'print.html', context)
