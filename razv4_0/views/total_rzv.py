from django.db.models import Min
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, datetime
from razv4_0.models import Driver, Customer, Razvozka, Razvozka_returns


def total_rzv(request):
    navi = 'razv'
    razvozki_plan = Razvozka.objects.filter(date=None, deleted=False).order_by('date_until').annotate(
        returned_all=Min('take__returned'))
    razvozki = Razvozka.objects.filter(date__isnull=False, deleted=False).order_by('-date', 'date_id').annotate(
        returned_all=Min('take__returned'))[:19]
    end_razvozki = Razvozka.objects.filter(date__isnull=False, deleted=False).order_by('-date', 'date_id').annotate(
        returned_all=Min('take__returned'))[19:20]
    razvozki = razvozki_plan.union(razvozki)
    customers = Customer.objects.all().order_by('name')
    drivers = Driver.objects.all().order_by('id')
    to_return = Razvozka.objects.filter(date__isnull=False, return_all=False, deliver_to=True,
                                                   fulfilled=True, customer__subcontractor=True, deleted=False).count()
    url_list = '/rzv/json_razvozki_list/'
    url_last = '/rzv/json_razvozki_last/'
    context = {'razvozki': razvozki, 'navi': navi, 'customers': customers, 'url_list': url_list, 'url_last': url_last,
               'drivers': drivers, 'to_return': to_return, 'end_razvozki': end_razvozki}
    return render(request, 'total_rzv.html', context)


def update_total_rzv(request):
    razv_id = request.POST['razv_id']
    if razv_id == '':
        razvozka = Razvozka(date_create=date.today())
    else:
        razvozka = Razvozka.objects.get(id=razv_id)
        if razvozka.fulfilled:
            return HttpResponse()
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
    return HttpResponse()
