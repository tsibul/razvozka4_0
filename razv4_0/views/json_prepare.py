import json
from datetime import datetime
from django.http import JsonResponse
from razv4_0.models import Razvozka, Razvozka_returns, Customer
from django.core.serializers import serialize
from django.db.models import Max


def razvozka_as_json(request, razv_id):
    razv = Razvozka.objects.get(id=razv_id).__dict__
#    json_razvozka = serialize('python', razv)
    json_razvozka = json.dumps(razv, ensure_ascii=False, default=str)
    return JsonResponse(json_razvozka, safe=False)


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