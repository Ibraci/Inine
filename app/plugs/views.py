from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rooms.models import Room
from rooms.models import Plug
from rooms.models import Bulb
from nanpy import (ArduinoApi, SerialManager)

# Create your views here.
@login_required
def index(request):
    plugs = Plug.objects.all()
    p = Plug.objects.all()
    rooms = Room.objects.all()

    return render(request, 'pages/plugs/index.html', {'plugs': plugs, 'rooms':rooms, 'p':p})

@login_required
def store(request):
    if request.method == 'POST':
        plug = Plug()
        plug.name = request.POST['name']
        plug.port = request.POST['port']
        plug.save()
        plug.room.add(request.POST['room'])
    return redirect('/plugs')

@login_required
def show(request, id):
    plug = Plug.objects.get(pk=id)
    p = ''
    for i in plug.room.all():
        p = i.id
    rooms = Room.objects.all()

    return render(request, 'pages/plugs/show.html', {'plug':plug, 'rooms':rooms, 'p': p})

@login_required
def edit(request, id):
    plug = Plug.objects.get(pk=id)
    p = ''
    for i in plug.room.all():
        p = i.id
    rooms = Room.objects.all()

    return render(request, 'pages/plugs/edit.html', {'plug':plug, 'rooms':rooms, 'p': p})

@login_required
def update(request, id):
    if request.method == 'POST':
        Plug.objects.select_related().filter(pk=id).update(name=request.POST['name'], port=request.POST['port'])
        plug = Plug.objects.get(pk=id)
        room = request.POST['room']
        plug.room.set([room])

    return redirect('/plugs')

@login_required
def destroy(request, id):
    plug = Plug.objects.get(pk=id)
    plug.delete()

    return redirect('/plugs')

@login_required
def checked(request, id):
    plug = Plug.objects.get(pk=id)
    port = plug.port
    ledPin = port
    try:
        connection = SerialManager()
        a = ArduinoApi(connection = connection)
        a.pinMode(ledPin, a.OUTPUT)
        ledState = a.LOW
        if request.method == 'POST':
            status = request.POST.get('status')
            if status == 'on':
                ledState = a.LOW
                status = True
            else:
                ledState = a.HIGH
                status = False

            Plug.objects.select_related().filter(pk=id).update(status=status)
            a.digitalWrite(ledPin, ledState)
        return redirect('/plugs')
    except:
        return redirect('/error/103')
