from django.shortcuts import render
from razv4_0.models import Customer, Razvozka


def customer(request):
    navi = 'customer'
    customers = Customer.objects.all().order_by('name')[:49]
    end_customer = Customer.objects.all()[49:50]
    to_return = Razvozka.objects.filter(date__isnull=False, return_all=False, deliver_to=True,
                                        fulfilled=True, customer__subcontractor=True).count()
    context = {'navi': navi, 'customers': customers, 'end_customer': end_customer, 'to_return': to_return}
    return render(request, 'customer.html', context)
