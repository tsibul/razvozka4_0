from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from razv4_0.models import Razvozka, Razvozka_returns, Customer
from datetime import date, timedelta


def current_rzv(request):
    navi = 'current'
    current_date = date.today()
    date_begin = current_date - timedelta(days=(current_date.weekday() + 7))
    date_end = current_date + timedelta(days=(14 - current_date.weekday()))
    razvozki = Razvozka.objects.filter(date__gt=date_begin, date__lte=date_end).order_by('-date', 'date_id')
    razvozki_plan = Razvozka.objects.filter(date=None).order_by('date_until')
    context = {'razvozki': razvozki, 'navi': navi, 'razvozki_plan': razvozki_plan}
    return render(request, 'current.html', context)

