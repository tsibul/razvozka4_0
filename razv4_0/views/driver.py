from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from razv4_0.models import Driver, DriverIcons, Razvozka


def driver(request):
    navi = 'diver'
    drivers = Driver.objects.filter(deleted=False).order_by('id')
    driver_icons = DriverIcons.objects.all().order_by('description')
    to_return = Razvozka.objects.filter(date__isnull=False, return_all=False, deliver_to=True,
                                        fulfilled=True, customer__subcontractor=True, deleted=False).count()
    context = {'navi': navi, 'to_return': to_return, 'drivers': drivers, 'driver_icons': driver_icons}
    return render(request, 'driver.html', context)


def driver_delete(request, drv_id):
    driver_to_delete = Driver.objects.get(id=drv_id)
    driver_to_delete.deleted = True
    driver_to_delete.save()
    return HttpResponseRedirect(reverse('razv4_0:driver'))