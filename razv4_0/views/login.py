from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/rzv/current')
        else:
            # Обработайте неправильные учетные данные, если необходимо
            pass
    return redirect('/rzv/current')


def custom_logout(request):
    logout(request)
    return redirect('/rzv/current')

#    return redirect('your_redirect_url')  # Замените 'your_redirect_url' на URL-адрес, на который перенаправлять после выхода
