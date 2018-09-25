from django.shortcuts import render
from rooms.models import Room, Bulb, Plug

def home(request):
    r = Room.objects.count()
    b = Bulb.objects.count()
    p = Plug.objects.count()
    return render(request, 'pages/home.html', {'r': r, 'b': b, 'p': p})
