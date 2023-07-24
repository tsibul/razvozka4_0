from razv4_0.models import Razvozka
from django.shortcuts import render


def print_all(request):
    context = {}
    return render(request, 'print.html', context)

def print_one(request, id):
    context = {}
    return render(request, 'print.html', context)
