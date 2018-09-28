from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import Account

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'auth/login.html')

def store(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/login')

@login_required
def profile(request):
    return render(request, 'auth/profile.html')

@login_required
def update(request):
    userid = request.POST['userid']
    if request.method == 'POST':
        user = request.user
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        if not phone.isdigit():
            raise ValidationError(('Le numero de telephone ne doit contenir que des chiffres'), code='invalid')
        Account.objects.select_related().filter(pk=userid).update(full_name=full_name, email=email, phone=phone)
    return redirect('/account/profile')

@login_required
def password(request):
    userid = request.POST['userid']
    account = Account.objects.get(pk=userid)
    if request.method == 'POST':
        if request.POST.get('newPassword') == request.POST.get('comfirmPassword'):
            account.set_password(request.POST['newPassword'])
        else:
            print("Les mots de passe de correspond pas !")
    return redirect('/account/profile')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/account/login')
