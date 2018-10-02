from django.shortcuts import render

# Create your views here.
def error103(request):
    return render(request, 'errors/103.html')

def error400(request):
    return render(request, 'errors/400.html', {}, status=400)

def error403(request):
    return render(request, 'errors/403.html', {}, status=403)

def error404(request):
    return render(request, 'errors/404.html', {}, status=404)

def error500(request):
    return render(request, 'errors/500.html', {}, status=500)
