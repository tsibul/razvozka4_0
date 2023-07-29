from django.shortcuts import render
from django.db.models import OuterRef, Subquery, F

from razv4_0.models import Driver, Customer, Razvozka


def total_rzv(request):
    navi = 'razv'
    razvozki_plan = Razvozka.objects.filter(date=None).order_by('date_until')
    razvozki = Razvozka.objects.filter(date__isnull=False).order_by('-date', 'date_id')[:19]
    end_razvozki = Razvozka.objects.filter(date__isnull=False).order_by('-date', 'date_id')[19:20]
    razvozki = razvozki_plan.union(razvozki)
    customers = Customer.objects.all().order_by('name')
    drivers = Driver.objects.all().order_by('id')
    to_return = Razvozka.objects.filter(date__isnull=False, return_all=False, deliver_to=True,
                                                   fulfilled=True, customer__subcontractor=True).count()
    context = {'razvozki': razvozki, 'navi': navi, 'customers': customers,
               'drivers': drivers, 'to_return': to_return, 'end_razvozki': end_razvozki}
    return render(request, 'total_rzv.html', context)
