from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from razv4_0.models import Razvozka, Razvozka_returns, Customer, Driver
from datetime import date, timedelta, datetime
from django.db.models import Min


def index(request):
    return HttpResponseRedirect(reverse('razv4_0:current_rzv'))


def current_rzv(request):
    navi = 'current'
    current_date = date.today()
    date_begin = current_date - timedelta(days=(current_date.weekday() + 7))
    date_end = current_date + timedelta(days=(14 - current_date.weekday()))
    razvozki = Razvozka.objects.filter(date__gte=date_begin, date__lt=date_end, deleted=False).order_by('-date',
                                                                                                        'date_id').annotate(
        returned_all=Min('take__deliver__return_all'))
    razvozki_plan = Razvozka.objects.filter(date=None, deleted=False).order_by('date_until')
    plan_number = razvozki_plan.count()
    customers = Customer.objects.filter(deleted=False).order_by('name')
    drivers = Driver.objects.filter(deleted=False).order_by('id')
    to_return = Razvozka.objects.filter(date__isnull=False, return_all=False, deliver_to=True,
                                        fulfilled=True, customer__subcontractor=True, deleted=False).count()

    context = {'razvozki': razvozki, 'navi': navi, 'razvozki_plan': razvozki_plan, 'customers': customers,
               'drivers': drivers, 'to_return': to_return, 'plan_number': plan_number}
    return render(request, 'current.html', context)


def update_rzv(request):
    razv_id = request.POST['razv_id']
    if razv_id == '':
        razvozka = Razvozka(date_create=date.today())
    else:
        razvozka = Razvozka.objects.get(id=razv_id)
        if razvozka.fulfilled:
            return HttpResponseRedirect(reverse('razv4_0:current_rzv'))
    if request.POST['date']:
        razvozka.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
    if request.POST['date_until']:
        razvozka.date_until = datetime.strptime(request.POST['date_until'], '%Y-%m-%d').date()
    razvozka.date_id = request.POST['date_id']
    if razvozka.date_id == '':
        razvozka.date_id = 0
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
    razvozka.save()
    rzv_return_quantity = int(request.POST['rzv_quantity'])
    j = 0
    if rzv_return_quantity:
        for i in range(0, rzv_return_quantity):
            razvozka_delivered = Razvozka.objects.get(id=request.POST['rzv_no_' + str(i)])
            try:
                razvozka_return = Razvozka_returns.objects.get(take=razvozka, deliver=razvozka_delivered, deleted=False)
            except:
                razvozka_return = Razvozka_returns(take=razvozka, deliver=razvozka_delivered)
            try:
                request.POST['rzv_check_' + str(i)]
                razvozka_return.save()
                razvozka.return_from = True
            except:
                j += 1
                if razvozka_return.id:
                    razvozka_return.deleted = True
                    razvozka_return.save()
    if j == rzv_return_quantity:
        razvozka.return_from = False
    razvozka.save()
    return HttpResponseRedirect(reverse('razv4_0:current_rzv'))


def razvozka_returned_all(request):
    razv_id = request.POST['razv_id']
    number_deliveries = int(request.POST['rzv_return_quantity'])
    for i in range(0, number_deliveries):
        deliver_id = request.POST['delivery-' + str(i)]
        razvozka_deliver = Razvozka.objects.get(id=deliver_id)
        razvozka_returns = Razvozka_returns.objects.get(take__id=razv_id, deliver=razvozka_deliver, deleted=False)
        try:
            request.POST['delivery-chk-' + str(i)]
            razvozka_deliver.return_all = True
            razvozka_returns.returned = True
        except:
            razvozka_deliver.return_all = False
            razvozka_returns.returned = False
        razvozka_deliver.save()
        razvozka_returns.save()
    return HttpResponse()
