from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from razv4_0.models import Razvozka, Razvozka_returns, Customer, Driver
from datetime import date, timedelta, datetime


def current_rzv(request):
    navi = 'current'
    current_date = date.today()
    date_begin = current_date - timedelta(days=(current_date.weekday() + 7))
    date_end = current_date + timedelta(days=(14 - current_date.weekday()))
    razvozki = Razvozka.objects.filter(date__gte=date_begin, date__lt=date_end).order_by('-date', 'date_id')
    razvozki_plan = Razvozka.objects.filter(date=None).order_by('date_until')
    customers = Customer.objects.all().order_by('name')
    drivers = Driver.objects.all().order_by('id')
    context = {'razvozki': razvozki, 'navi': navi, 'razvozki_plan': razvozki_plan, 'customers': customers,
               'drivers': drivers}
    return render(request, 'current.html', context)


def update_rzv(request):
    razv_id = request.POST['razv_id']
    if razv_id == '':
        razvozka = Razvozka(date_create=date.today())
    else:
        razvozka = Razvozka.objects.get(id=razv_id)
        if razvozka.fulfilled:
            return HttpResponseRedirect(reverse('razv4_0:current_rzv'))
    razvozka.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
    razvozka.date_until = datetime.strptime(request.POST['date_until'], '%Y-%m-%d').date()
    razvozka.date_id = request.POST['date_id']
    razvozka.customer_name = request.POST['customer_name']
    razvozka.address = request.POST['address']
    razvozka.contact = request.POST['contact']
    razvozka.map_point = request.POST['map_point']
    razvozka.to_do_take = request.POST['to_do_take']
    razvozka.to_do_deliver = request.POST['to_do_deliver']
    customer_id = request.POST['customer_id']
    if customer_id != '':
        razvozka.customer = Customer.objects.get(id=customer_id)
    razvozka.driver = Driver.objects.get(id=request.POST['driver'])
    rzv_return_quantity = int(request.POST['rzv_quantity'])
    j = 0
    if rzv_return_quantity:
        for i in range(0, rzv_return_quantity):
            razvozka_delivered = Razvozka.objects.get(id=request.POST['rzv_no_' + str(i)])
            try:
                razvozka_return = Razvozka_returns.objects.get(take=razvozka, deliver=razvozka_delivered)
            except:
                razvozka_return = Razvozka_returns(take=razvozka, deliver=razvozka_delivered)
            try:
                request.POST['rzv_check_' + str(i)]
                razvozka_return.save()
                razvozka.return_from = True
            except:
                j += 1
                if razvozka_return.id:
                    razvozka_return.delete()
    if j == rzv_return_quantity:
        razvozka.return_from = False
    razvozka.save()
    return HttpResponseRedirect(reverse('razv4_0:current_rzv'))
