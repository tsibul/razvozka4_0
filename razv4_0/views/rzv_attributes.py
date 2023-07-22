from django.http import HttpResponseRedirect
from django.urls import reverse

from razv4_0.models import Razvozka, Razvozka_returns, Customer


def razvozka_fulfilled(request, razv_id):
    return HttpResponseRedirect(reverse('razv4_0: current_rzv'))


def razvozka_unfulfilled(request, razv_id):
    return HttpResponseRedirect(reverse('razv4_0: current_rzv'))


def razvozka_returned_all(request, razv_id):
    return HttpResponseRedirect(reverse('razv4_0: current_rzv'))


def razvozka_deliver_to(request, razv_id):
    return HttpResponseRedirect(reverse('razv4_0: current_rzv'))
