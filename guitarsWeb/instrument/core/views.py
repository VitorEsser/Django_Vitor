from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Instrument
from django.contrib.auth import logout
# Create your views here.

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def set_instrument(request):
    name = request.POST.get('name')
    brand = request.POST.get('brand')
    strings = request.POST.get('strings')
    file = request.FILES.get('file')
    user = request.user
    instrument_id = request.POST.get('instrument_id')
    if instrument_id:
        instrument = instrument.objects.get(id=instrument_id)
        if user == instrument.user:
            instrument.name = name
            instrument.brand = brand
            instrument.strings = strings
            if file:
                instrument.photo = file
            instrument.save()
    else:
        instrument = Instrument.objects.create(name=name, brand=brand, strings=strings, user=user, photo=file)
    url = '/instrument/detail/{}/'.format(instrument.id)
    return redirect(url)

@login_required(login_url='/login/')
def register_instrument(request):
    instrument_id = request.GET.get('id')
    if instrument_id:
        instrument = Instrument.objects.get(id=instrument_id)
        if instrument.user == request.user:
            return render(request, 'register-instrument.html', {'instrument':instrument})
    return render(request, 'register-instrument.html')

@login_required(login_url='/login/')
def instrument_detail(request, id):
    instrument = Instrument.objects.get(active=True, id=id)
    return render(request, 'instrument.html', {'instrument':instrument})

@login_required(login_url='/login/')
def list_all_instrument(request):
    instrument = Instrument.objects.filter(active=True)
    return render(request, 'list.html', {'instrument':instrument})

@login_required(login_url='/login/')
def list_user_instrument(request):
    instrument = Instrument.objects.filter(active=True, user=request.user)
    return render(request, 'list.html', {'instrument':instrument})

@login_required(login_url='/login/')
def delete_instrument(request, id):
    instrument = Instrument.objects.get(id=id)
    if instrument.user == request.user:
        instrument.delete()
    return redirect('/')

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/instrument/all/')
        else:
            messages.error(request, 'OPS! Usuário/Senha inválidos. Por favor, tente novamente.')
    return redirect('/login/')

