from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse

from razv4_0.models import Razvozka, ImportRazvozka, ImportCustomer, Customer, Razvozka_returns


def admin(request):
    navi = 'admin'
    to_return = Razvozka.objects.filter(date__isnull=False, return_all=False, deliver_to=True,
                                        fulfilled=True, customer__subcontractor=True, deleted=False).count()
    context = {'navi': navi, 'to_return': to_return}

    return render(request, 'admin.html', context)


def admin_import(request):
    ImportCustomer.objects.all().delete()
    ImportRazvozka.objects.all().delete()
    rzv_sql_path = 'razv4_0/static/razvozki4_0/files/razvozka.sql'
    cst_sql_path = 'razv4_0/static/razvozki4_0/files/customer.sql'
    drv_sql_path = 'razv4_0/static/razvozki4_0/files/driver.sql'
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
    with open(drv_sql_path, 'r', encoding='utf-8') as drv_file:
        drv_queries = drv_file.read()
    with connection.cursor() as cursor:
        cursor.execute(drv_queries)
    admin_transfer()
    return HttpResponseRedirect(reverse('razv4_0:admin'))


def admin_delete_all():
    Razvozka.objects.all().delete()
    Customer.objects.all().delete()
    Razvozka_returns.objects.all().delete()


def admin_transfer():
    admin_delete_all()
    import_customers = ImportCustomer.objects.all()
    customer_list = []
    for import_customer in import_customers:
        customer_list.append(Customer(id=import_customer.id, name=import_customer.name, address=import_customer.address,
                                      contact=import_customer.contact, mappoint=import_customer.mappoint,
                                      subcontractor=import_customer.subcontractor))
    Customer.objects.bulk_create(customer_list)
    import_razvozka = ImportRazvozka.objects.all()
    razvozka_list = []
    for rzv in import_razvozka:
        razvozka = Razvozka(id=rzv.id, date=rzv.date, date_id=rzv.date_id,
                            customer_name=rzv.customer_name, address=rzv.address, contact=rzv.contact,
                            to_do_deliver=rzv.to_do_deliver, to_do_take=rzv.to_do_take,
                            map_point=rzv.map_point, fulfilled=rzv.fulfilled, deliver_to=rzv.deliver_to,
                            return_from=rzv.return_from, return_all=rzv.return_all, date_until=rzv.date_until,
                            date_create=rzv.date_create)
        try:
            customer = Customer.objects.get(id=rzv.customer.id)
            razvozka.customer = customer
        except:
            pass
        razvozka_list.append(razvozka)
    Razvozka.objects.bulk_create(razvozka_list)
    return_list = []
    return_razvozka = ImportRazvozka.objects.filter(return_goods__isnull=False)
    for return_rzv in return_razvozka:
        take = Razvozka.objects.get(id=return_rzv.id)
        deliver = Razvozka.objects.get(id=return_rzv.return_goods.id)
        razvozka_return = Razvozka_returns(take=take, deliver=deliver, returned=deliver.return_all)
        return_list.append(razvozka_return)
    Razvozka_returns.objects.bulk_create(return_list)
