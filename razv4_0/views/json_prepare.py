import json
from datetime import datetime
from django.http import JsonResponse
from razv4_0.models import Razvozka, Razvozka_returns, Customer, Driver
from django.core.serializers import serialize
from django.db.models import Max, Min, Q


def razvozka_as_json(request, razv_id):
    razv = Razvozka.objects.get(id=razv_id).__dict__
    json_razvozka = json.dumps(razv, ensure_ascii=False, default=str)
    return JsonResponse(json_razvozka, safe=False)


def customer_as_json(request, cst_id):
    cst = Customer.objects.get(id=cst_id).__dict__
    json_customer = json.dumps(cst, ensure_ascii=False, default=str)
    return JsonResponse(json_customer, safe=False)


def customers_as_json(request):
    customers = Customer.objects.all().order_by('name')
    json_customers = serialize('python', customers)
    json_customers = json.dumps(json_customers, ensure_ascii=False)
    return JsonResponse(json_customers, safe=False)


def open_deliveries_as_json(request):
    deliveries = Razvozka.objects.filter(deliver_to=True, return_all=False)
    json_deliveries = serialize('python', deliveries)
    json_deliveries = json.dumps(json_deliveries, ensure_ascii=False, default=str)
    return JsonResponse(json_deliveries, safe=False)


def deliveries_as_json(request, cust_id):
    deliveries = Razvozka.objects.filter(deliver_to=True, return_all=False, customer__id=cust_id)
    json_deliveries = serialize('python', deliveries)
    json_deliveries = json.dumps(json_deliveries, ensure_ascii=False, default=str)
    return JsonResponse(json_deliveries, safe=False)


def data_id_as_json(request, date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    try:
        date_id = Razvozka.objects.filter(date=date).aggregate(Max('date_id'))['date_id__max'] + 1
    except:
        date_id = 1
    return JsonResponse(date_id, safe=False)


def customer_name_as_json(request, cst_id):
    customer_name = Customer.objects.get(id=cst_id).name
    return JsonResponse(customer_name, safe=False)


def driver_icon_as_json(request, driver_id):
    icon_url = '/static/' + Driver.objects.get(id=driver_id).icon_code
    return JsonResponse(icon_url, safe=False)


def driver_description_as_json(request, driver_id):
    description_url = Driver.objects.get(id=driver_id).description
    return JsonResponse(description_url, safe=False)


def returns_as_id_json(request, razv_id):
    returns = list(Razvozka_returns.objects.filter(take__id=razv_id).values_list('deliver__id', flat=True))
    return JsonResponse(returns, safe=False)


def returns_as_json(request, razv_id):
    returns = list(Razvozka_returns.objects.filter(take__id=razv_id).values(
        'deliver__id', 'deliver__date', 'deliver__to_do_deliver', 'deliver__return_all'))
    return JsonResponse(returns, safe=False)


def razvozki_list_as_json(request, last_element):
    razvozki_query = Razvozka.objects.filter(date__isnull=False).order_by('-date', 'date_id').annotate(
        returned_all=Min('take__deliver__return_all'))[last_element:last_element + 19]
    razvozki = serialize('python', razvozki_query)
    razvozki = json.dumps(razvozki, ensure_ascii=False, default=str)
    return JsonResponse(razvozki, safe=False)


def razvozki_last_list_as_json(request, last_element):
    razvozki_query = Razvozka.objects.filter(date__isnull=False).order_by('-date', 'date_id').annotate(
        returned_all=Min('take__deliver__return_all'))[last_element + 19:last_element + 20]
    razvozki = serialize('python', razvozki_query)
    razvozki = json.dumps(razvozki, ensure_ascii=False, default=str)
    return JsonResponse(razvozki, safe=False)


def returned_all_as_json(request, razv_id):

    returned_all = Razvozka_returns.objects.filter(take_id=razv_id)
    if returned_all.count():
        returned_all = returned_all.annotate(minimum=Min('deliver__return_all')).values('minimum')[0]['minimum']
    else:
        returned_all = False
    return JsonResponse(returned_all, safe=False)


def search_razvozki_list_as_json(request, search_string, last_element):
    razvozki_query = Razvozka.objects.filter(Q(customer_name__icontains=search_string) |
                                             Q(address__icontains=search_string) |
                                             Q(contact__icontains=search_string) |
                                             Q(to_do_take__icontains=search_string) |
                                             Q(to_do_deliver__icontains=search_string)).order_by('-date')[last_element: last_element + 19]
    razvozki = serialize('python', razvozki_query)
    razvozki = json.dumps(razvozki, ensure_ascii=False, default=str)
    return JsonResponse(razvozki, safe=False)


def search_razvozki_last_as_json(request, search_string, last_element):
    razvozki_query = Razvozka.objects.filter(Q(customer_name__icontains=search_string) |
                                             Q(address__icontains=search_string) |
                                             Q(contact__icontains=search_string) |
                                             Q(to_do_take__icontains=search_string) |
                                             Q(to_do_deliver__icontains=search_string))[last_element + 19: last_element + 20]
    razvozki = serialize('python', razvozki_query)
    razvozki = json.dumps(razvozki, ensure_ascii=False, default=str)
    return JsonResponse(razvozki, safe=False)
