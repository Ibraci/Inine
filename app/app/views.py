from django.shortcuts import render
from rooms.models import Room, Bulb, Plug
from django.contrib.auth import authenticate

def home(request):
    if request.user.is_authenticated:
        r = Room.objects.count()
        b = Bulb.objects.count()
        p = Plug.objects.count()
        return render(request, 'pages/home.html', {'r': r, 'b': b, 'p': p})
    else:
        return redirect('/account/login')

def store(request):
    pass
