from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'razv4_0'

urlpatterns = [
    path('accounts/login/', views.custom_login, name='custom_login'),
    path('accounts/logout/', views.custom_logout, name='custom_logout'),

    path('current/', views.current_rzv, name='current_rzv'),
    path('current/razvozka_delete/<int:razv_id>', views.razvozka_delete, name='razvozka_delete'),
    path('current/razvozka_fulfilled/<int:razv_id>', views.razvozka_fulfilled, name='razvozka_fulfilled'),
    path('current/razvozka_returned_all/<int:razv_id>', views.razvozka_returned_all, name='razvozka_returned_all'),
    path('razvozka_deliver_to/<int:razv_id>', views.razvozka_returned_all, name='razvozka_deliver_to'),

]

