from django.shortcuts import render
from razv4_0.models import Customer


def customer(request):
    navi = 'customer'
    customers = Customer.objects.all().order_by('name')[:49]
    end_customer = Customer.objects.all()[49:50]
    context = {'navi': navi, 'customers': customers, 'end_customer': end_customer}
    return render(request, 'customer.html', context)
