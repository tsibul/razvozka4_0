from django.shortcuts import render

from razv4_0.models import Driver, Customer, Razvozka


def deliver_no_return(request):
    navi = 'deliver'
    razvozki = Razvozka.objects.filter(date__isnull=False, return_all=False, deliver_to=True,
                                       customer__subcontractor=True).order_by('-date', 'date_id')[:50]
    customers = Customer.objects.all().order_by('name')
    drivers = Driver.objects.all().order_by('id')
    context = {'razvozki': razvozki, 'navi': navi, 'customers': customers, 'drivers': drivers}
    return render(request, 'total_rzv.html', context)
