from django.shortcuts import render, HttpResponse
from razv4_0.models import Customer, Razvozka


def customer_list(request):
    navi = 'customer'
    customers = Customer.objects.filter(deleted=False).order_by('name')[:49]
    end_customer = Customer.objects.filter(deleted=False)[49:50]
    to_return = Razvozka.objects.filter(date__isnull=False, return_all=False, deliver_to=True,
                                        fulfilled=True, customer__subcontractor=True, deleted=False).count()
    context = {'navi': navi, 'customers': customers, 'end_customer': end_customer, 'to_return': to_return}
    return render(request, 'customer.html', context)


def customer_update(request):
    customer_id = request.POST['cst_id']
    name = request.POST['name']
    address = request.POST['address']
    contact = request.POST['contact']
    subcontractor = request.POST['subcontractor']
    if subcontractor == 'false':
        subcontractor = False
    else:
        subcontractor = True
    if customer_id != 'undefined':
        customer = Customer.objects.get(id=customer_id)
        customer.name = name
    else:
        customer = Customer(name=name)
    customer.address = address
    customer.contact = contact
    customer.subcontractor = subcontractor
    customer.save()
    return HttpResponse()
