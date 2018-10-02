from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rooms.models import Room
from rooms.models import Bulb
from nanpy import (ArduinoApi, SerialManager)

# Create your views here.
@login_required
def index(request):
    bulbs = Bulb.objects.all()
    rooms = Room.objects.all()
    connect = Bulb.objects.get(pk=1)

    return render(request, 'pages/bulbs/index.html', {'bulbs': bulbs, 'rooms':rooms, 'connect':connect})

@login_required
def store(request):
    if request.method == 'POST':
        bulb = Bulb()
        bulb.name = request.POST['name']
        bulb.port = request.POST['port']
        bulb.port_connect = request.POST['port_connect']
        bulb.save()
        bulb.room.add(request.POST['room'])
    return redirect('/bulbs')

@login_required
def show(request, id):
    bulb = Bulb.objects.get(pk=id)
    b = ''
    for i in bulb.room.all():
        b = i.id
    rooms = Room.objects.all()

    return render(request, 'pages/bulbs/show.html', {'bulb':bulb, 'rooms':rooms, 'b': b})

@login_required
def edit(request, id):
    bulb = Bulb.objects.get(pk=id)
    b = ''
    for i in bulb.room.all():
        b = i.id
    rooms = Room.objects.all()

    return render(request, 'pages/bulbs/edit.html', {'bulb':bulb, 'rooms':rooms, 'b': b})

@login_required
def update(request, id):
    if request.method == 'POST':
        Bulb.objects.select_related().filter(pk=id).update(name=request.POST['name'], port=request.POST['port'], port_connect=request.POST['port_connect'])
        bulb = Bulb.objects.get(pk=id)
        room = request.POST['room']
        bulb.room.set([room])

    return redirect('/bulbs')

@login_required
def destroy(request, id):
    bulb = Bulb.objects.get(pk=id)
    bulb.delete()

    return redirect('/bulbs')

@login_required
def checked(request, id):
    bulb = Bulb.objects.get(pk=id)
    port = bulb.port
    ledPin = port
    try:
        connection = SerialManager()
        a = ArduinoApi(connection = connection)
        a.pinMode(ledPin, a.OUTPUT)
        ledState = a.LOW
        if request.method == 'POST':
            status = request.POST.get('status')
            if status == 'on':
                ledState = a.HIGH
                status = True
            else:
                ledState = a.LOW
                status = False

            Bulb.objects.select_related().filter(pk=id).update(status=status)
            a.digitalWrite(ledPin, ledState)
        return redirect('/bulbs')
    except:
        return redirect('/error/103')

@login_required
def connect(request):
    try:
        connection = SerialManager()
        a = ArduinoApi(connection = connection)
        ledState = a.LOW

        if request.method == 'POST':
            connect = request.POST.get('connect')
            if connect == 'on':
                value = True
                status = True
                ledState = a.HIGH
            else:
                value = False
                status = False
                ledState = a.LOW

            Bulb.objects.all().update(connect=value, status=status)
            bulbs = Bulb.objects.all()
            for bulb in bulbs:
                ledPin = bulb.port_connect
                ledPin1 = bulb.port
                a.pinMode(ledPin, a.OUTPUT)
                a.pinMode(ledPin1, a.OUTPUT)
                a.digitalWrite(ledPin, ledState)
                a.digitalWrite(ledPin1, ledState)
        return redirect('/bulbs')
    except:
        return redirect('/error/103')
