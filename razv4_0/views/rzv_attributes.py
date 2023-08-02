from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from razv4_0.models import Razvozka, Razvozka_returns, Customer


def razvozka_fulfilled(request, razv_id):
    razv = Razvozka.objects.get(id=razv_id)
    razv.fulfilled = not razv.fulfilled
    razv.save()
    return HttpResponse()


def razvozka_deliver_to(request, razv_id):
    razv = Razvozka.objects.get(id=razv_id)
    razv.deliver_to = not razv.deliver_to
    razv.save()
    return HttpResponse()


def razvozka_delete(request, razv_id):
    razv_to_delete = Razvozka.objects.get(id=razv_id)
    if not razv_to_delete.fulfilled:
        razv_to_delete.deleted = True
        razv_to_delete.save()
    return HttpResponse()
