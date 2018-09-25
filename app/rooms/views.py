from django.shortcuts import render, redirect
from rooms.models import Room
from rooms.models import Plug
from rooms.models import Bulb

# Create your views here.
def index(request):
    rooms = Room.objects.all()

    return render(request, 'pages/rooms/index.html', {'rooms':rooms})

def show(request, id):
    room = Room.objects.get(pk=id)
    prises = Plug.objects.filter(room=id)
    bulbs = Bulb.objects.filter(room=id)

    return render(request, 'pages/rooms/show.html', {'room':room, 'plugs':prises, 'bulbs':bulbs})

def store(request):
    if request.method == 'POST':
        r = Room()
        r.name = request.POST['name']
        r.save()
    return redirect('/rooms')

def edit(request, id):
    room = Room.objects.get(pk=id)

    return render(request, 'pages/rooms/edit.html', {'room':room})

def update(request, id):
    Room.objects.select_related().filter(pk=id).update(name=request.POST['name'])
    return redirect('/rooms')

def destroy(request, id):
    room = Room.objects.get(pk=id)
    room.delete()

    return redirect('/rooms')
