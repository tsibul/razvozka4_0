from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'razv4_0'

urlpatterns = [
    path('accounts/login/', views.custom_login, name='custom_login'),
    path('accounts/logout/', views.custom_logout, name='custom_logout'),

    path('', views.index, name='index'),
    path('current/', views.current_rzv, name='current_rzv'),
    path('current_update', views.update_rzv, name='update_current'),
    path('razvozka_update', views.update_total_rzv, name='update_rzv'),
    path('search_rzv', views.search_all, name='search_rzv'),

    path('customer/', views.customer_list, name='customer'),
    path('customer_update/', views.customer_update, name='customer_update'),
    path('customer_delete/<int:cust_id>', views.customer_delete, name='customer_delete'),

    path('driver/', views.driver, name='driver'),
    path('driver_delete/<int:drv_id>', views.driver_delete, name='driver_delete'),
    path('driver_update', views.driver_update, name='driver_update'),

    path('admin/', views.admin, name='admin'),
    path('admin_import/', views.admin_import, name='admin_import'),

    path('razvozki/', views.total_rzv, name='total_rzv'),
    path('deliver_no_return/', views.deliver_no_return, name='deliver_no_return'),
    path('deliver_close/', views.close_delivered, name='close_delivered'),

    path('print/<str:date_rzv>', views.print_all, name='print_all'),
    path('print/<str:date_rzv>/<int:driver_id>', views.print_one, name='print_one'),

    path('razvozka_delete/<int:razv_id>', views.razvozka_delete, name='razvozka_delete'),
    path('razvozka_fulfilled/<razv_id>', views.razvozka_fulfilled, name='razvozka_fulfilled'),
    path('razvozka_returned_all/', views.razvozka_returned_all, name='razvozka_returned_all'),
    path('razvozka_deliver_to/<int:razv_id>', views.razvozka_deliver_to, name='razvozka_deliver_to'),

    path('json_razvozka/<int:razv_id>', views.razvozka_as_json),
    path('json_customer_select/<int:cst_id>', views.customer_as_json),
    path('json_driver_select/<int:drv_id>', views.driver_as_json),
    path('json_customer/', views.customers_as_json),
    path('json_open_deliveries/', views.open_deliveries_as_json),
    path('json_deliveries/<int:cust_id>', views.deliveries_as_json),
    path('json_date_id/<str:date_str>', views.data_id_as_json),
    path('json_customer_name/<int:cst_id>', views.customer_name_as_json),
    path('json_driver_url/<int:driver_id>', views.driver_icon_as_json),
    path('json_driver_url_from_url/<str:drv_url>', views.driver_icon_from_url_as_json),
    path('json_driver_description/<int:driver_id>', views.driver_description_as_json),
    path('json_returns/<int:razv_id>', views.returns_as_id_json),
    path('json_returns_full_info/<int:razv_id>', views.returns_as_json),
    path('json_return_all_min/<int:razv_id>', views.returned_all_as_json),
    path('json_deliver/<int:razv_id>', views.deliver_list_as_json),

    path('json_razvozki_list/<int:last_element>', views.razvozki_list_as_json),
    path('json_razvozki_last/<int:last_element>', views.razvozki_last_list_as_json),
    path('json_customers_list/<int:last_element>', views.customer_list_as_json),
    path('json_customers_last/<int:last_element>', views.customer_last_as_json),

    path('json_search_rzv_list/<str:search_string>/<int:last_element>', views.search_razvozki_list_as_json),
    path('json_search_rzv_last/<str:search_string>/<int:last_element>', views.search_razvozki_last_as_json),

]

