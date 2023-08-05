from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse

from razv4_0.models import Razvozka


def admin(request):
    navi = 'admin'
    to_return = Razvozka.objects.filter(date__isnull=False, return_all=False, deliver_to=True,
                                                   fulfilled=True, customer__subcontractor=True, deleted=False).count()
    context = {'navi': navi, 'to_return': to_return}

    return render(request, 'admin.html', context)


def admin_import(request):
    rzv_sql_path = 'razv4_0/static/razvozki4_0/files/razvozka.sql'
    cst_sql_path = 'razv4_0/static/razvozki4_0/files/customer.sql'
    with open(cst_sql_path, 'r', encoding='utf-8') as cst_file:
        cst_queries = cst_file.read()
    cst_queries = cst_queries.replace('INSERT INTO `razvozki_customer`', 'INSERT INTO `razv4_0_importcustomer`')
    with connection.cursor() as cursor:
        cursor.execute(cst_queries)
    with open(rzv_sql_path, 'r', encoding='utf-8') as rzv_file:
        rzv_queries = rzv_file.read()
    rzv_queries = rzv_queries.replace('INSERT INTO `razvozki_razvozka`', 'INSERT INTO `razv4_0_importrazvozka`')
    with connection.cursor() as cursor:
        cursor.execute(rzv_queries)
    return HttpResponseRedirect(reverse('razv4_0:admin'))
