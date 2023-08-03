import json

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from razv4_0.models import Driver, DriverIcons, Razvozka


def driver(request):
    navi = 'diver'
    drivers = Driver.objects.filter(deleted=False).order_by('id')
    driver_icons = DriverIcons.objects.all().order_by('id')
    to_return = Razvozka.objects.filter(date__isnull=False, return_all=False, deliver_to=True,
                                        fulfilled=True, customer__subcontractor=True, deleted=False).count()
    context = {'navi': navi, 'to_return': to_return, 'drivers': drivers, 'driver_icons': driver_icons}
    return render(request, 'driver.html', context)


def driver_delete(request, drv_id):
    driver_to_delete = Driver.objects.get(id=drv_id)
    driver_to_delete.deleted = True
    driver_to_delete.save()
    return HttpResponseRedirect(reverse('razv4_0:driver'))


def driver_update(request):
    drv_id = request.POST['drv_id']
    description = request.POST['description']
    code = request.POST['code']
    phone1 = request.POST['phone1']
    phone2 = request.POST['phone2']
    car_no = request.POST['car_no']
    if drv_id:
        driver_to_update = Driver.objects.get(id=drv_id)
        driver_to_update.description = description
    else:
        driver_to_update = Driver(description=description)
    driver_to_update.code = code
    driver_to_update.phone1 = phone1
    driver_to_update.phone2 = phone2
    driver_to_update.car_no = car_no
    # icons_quantity = DriverIcons.objects.all().count()
    # for i in range(1, icons_quantity + 1):
    #     try:
    #         request.POST['chk-' + str(i)]
    #         driver_to_update.icon_code = request.POST['url-' + str(i)]
    #     except:
    #         pass
    driver_to_update.save()
    return HttpResponseRedirect(reverse('razv4_0:driver'))


def driver_as_json(request, drv_id):
    drv = Driver.objects.get(id=drv_id).__dict__
    json_driver = json.dumps(drv, ensure_ascii=False, default=str)
    return JsonResponse(json_driver, safe=False)


def driver_icon_from_url_as_json(request, drv_url):
    drv_icon = DriverIcons.objects.get(icon_url=drv_url).__dict__
    json_driver_icon = json.dumps(drv_icon, ensure_ascii=False, default=str)
    return JsonResponse(json_driver_icon, safe=False)
