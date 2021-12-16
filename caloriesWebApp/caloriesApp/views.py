import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import *
from caloriesApp.models import *


# Create your views here.

@login_required(login_url='login')
def homepage(request):
    # print(type(render))
    all_mancat = Mancat.objects.filter(username=request.user, data=datetime.date.today())
    total = 0
    for articol in all_mancat:
        articol.calorii = articol.articole_mancate.calorii * articol.amount/100
        total += articol.calorii
    ramas = 2500 - total

    if request.method == 'POST':
        Profil.objects.create(username=request.user, zi=datetime.date.today(), calorii=total)
        return HttpResponseRedirect('/')

    return render(request, 'homepage.html', {
        'mancate': all_mancat,
        'total': total,
        'ramas': ramas
    })


@login_required(login_url='login')
def adauga_produs(request):
    articole = Articol.objects.order_by('nume')

    if request.method == 'POST':
        articol = request.POST.get('id_articol')
        amount = request.POST.get('amount')
        user = request.user
        data = datetime.date.today()
        Mancat.objects.create(username=user, amount=amount, articole_mancate=Articol.objects.get(id=articol), data=data)
        return redirect('/adaugaProdus')
    else:
        return render(request, 'adauga_produs.html', {
            'articole': articole
        })


@login_required(login_url='login')
def toate_produsele(request):
    produse = Articol.objects.order_by('nume')
    return render(request, 'toate_produsele.html', {
        'produse': produse
    })


@login_required(login_url='login')
def creaza_produs(request):
    if request.method == 'POST':
        form = AdaugaArticol(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/toateProdusele')
    else:
        form = AdaugaArticol()
        return render(request, 'creaza_produs.html', {
            'form': form
        })


@login_required(login_url='login')
def profil(request):
    utilizator = User.objects.get_by_natural_key(request.user)
    profil_user = Profil.objects.filter(username=request.user)
    return render(request, 'profil.html', {
        'utilizator': utilizator,
        'profil': profil_user
    })


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is invalid')
    return render(request, 'login.html')


@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('login')


