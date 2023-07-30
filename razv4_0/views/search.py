from django.db.models import Q
from django.shortcuts import render
from razv4_0.models import Razvozka, Customer, Driver


def search_all(request):
    navi = request.POST['navi']
    search_string = request.POST['search_string']
    if navi == 'current' or navi == 'razv' or navi == 'deliver':
        razvozki = Razvozka.objects.filter(Q(customer_name__icontains=search_string) |
                                           Q(address__icontains=search_string) |
                                           Q(contact__icontains=search_string) |
                                           Q(to_do_take__icontains=search_string) |
                                           Q(to_do_deliver__icontains=search_string)).order_by('-date')[:19]
        end_razvozki = Razvozka.objects.filter(Q(customer_name__icontains=search_string) |
                                               Q(address__icontains=search_string) |
                                               Q(contact__icontains=search_string) |
                                               Q(to_do_take__icontains=search_string) |
                                               Q(to_do_deliver__icontains=search_string))[19:20]
        customers = Customer.objects.all().order_by('name')
        drivers = Driver.objects.all().order_by('id')
        to_return = Razvozka.objects.filter(date__isnull=False, return_all=False, deliver_to=True,
                                            fulfilled=True, customer__subcontractor=True).count()
        url_list = '/rzv/json_search_rzv_list/' + search_string + '/'
        url_last = '/rzv/json_search_rzv_last/' + search_string + '/'

        context = {'razvozki': razvozki, 'navi': navi, 'customers': customers, 'url_list': url_list, 'url_last': url_last,
                   'drivers': drivers, 'to_return': to_return, 'end_razvozki': end_razvozki}
    else:
        context = {'navi': navi}
    return render(request, 'total_rzv.html', context)
