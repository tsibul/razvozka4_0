from django.shortcuts import render
from django.db.models import OuterRef, Subquery, F

from razv4_0.models import Driver, Customer, Razvozka


def total_rzv(request):
    navi = 'razv'
    razvozki_plan = Razvozka.objects.filter(date=None).order_by('date_until')
    razvozki = Razvozka.objects.filter(date__isnull=False).order_by('-date', 'date_id')[:50]
    razvozki = razvozki_plan.union(razvozki)
    customers = Customer.objects.all().order_by('name')
    drivers = Driver.objects.all().order_by('id')
    context = {'razvozki': razvozki, 'navi': navi, 'customers': customers,
               'drivers': drivers}
    return render(request, 'total_rzv.html', context)
