from django.shortcuts import render
from razv4_0.models import Driver, DriverIcons, Razvozka


def driver(request):
    navi = 'diver'
    drivers = Driver.objects.all().order_by('id')
    driver_icons = DriverIcons.objects.all().order_by('description')
    to_return = Razvozka.objects.filter(date__isnull=False, return_all=False, deliver_to=True,
                                        fulfilled=True, customer__subcontractor=True).count()
    context = {'navi': navi, 'to_return': to_return, 'drivers': drivers, 'driver_icons': driver_icons}
    return render(request, 'driver.html', context)
