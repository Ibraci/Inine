from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rooms.models import Room
from rooms.models import Plug
from rooms.models import Bulb

# Create your views here.

@login_required
def index(request):
    rooms = Room.objects.all()

    return render(request, 'pages/rooms/index.html', {'rooms':rooms})

@login_required
def show(request, id):
    room = Room.objects.get(pk=id)
    prises = Plug.objects.filter(room=id)
    bulbs = Bulb.objects.filter(room=id)

    return render(request, 'pages/rooms/show.html', {'room':room, 'plugs':prises, 'bulbs':bulbs})

@login_required
def store(request):
    if request.method == 'POST':
        r = Room()
        r.name = request.POST['name']
        r.save()
    return redirect('/rooms')

@login_required
def edit(request, id):
    room = Room.objects.get(pk=id)

    return render(request, 'pages/rooms/edit.html', {'room':room})

@login_required
def update(request, id):
    Room.objects.select_related().filter(pk=id).update(name=request.POST['name'])
    return redirect('/rooms')

@login_required
def destroy(request, id):
    room = Room.objects.get(pk=id)
    room.delete()

    return redirect('/rooms')
