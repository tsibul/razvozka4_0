from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime

from razv4_0.models import Driver, Customer, Razvozka


def deliver_no_return(request):
    navi = 'deliver'

    razvozki = Razvozka.objects.filter(date__isnull=False, return_all=False, deliver_to=True, fulfilled=True,
                                       customer__subcontractor=True, deleted=False).order_by('-date', 'date_id')
    to_return = razvozki.count()
    customers = Customer.objects.filter(deleted=False).order_by('name')
    drivers = Driver.objects.filter(deleted=False).order_by('id')
    context = {'razvozki': razvozki, 'navi': navi, 'customers': customers, 'drivers': drivers, 'to_return': to_return}
    return render(request, 'delivered.html', context)


def close_delivered(request):
    date = datetime.date.today()
    rzv_id = request.POST['rzv_id']
    comment = request.POST['return_close_without_delivery']
    razvozka = Razvozka.objects.get(id=rzv_id)
    razvozka.return_all = True
    razvozka.return_close_without_delivery = comment
    razvozka.return_close_date = date
    razvozka.save()
    return HttpResponseRedirect(reverse('razv4_0:deliver_no_return'))
