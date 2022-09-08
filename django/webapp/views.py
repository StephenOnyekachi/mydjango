from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Testimony
from .models import Address
from .models import Users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import TestimonyForm
from .forms import AddressForm
from .forms import SignupForm
from .forms import UsersForm

# Create your views here.

def home(request):
    address = Address.objects.all()
    context = {
        'address': address
    }
    return render(request, 'home.html', context)

def index(request):
    context = {
    }
    return render(request, 'adminpage.html', context)

def admintestimone(request):
    if request.method == 'POST':
        testimony_form = TestimonyForm(request.POST)
        if testimony_form.is_valid():
            testimony_form.save()
            return redirect('admintestimone')
    else:
        testimony_form = TestimonyForm()

    testimony = Testimony.objects.all()
    context = {
        'testimony_form': testimony_form,
        'testimony': testimony,
    }
    return render(request, 'admintestimone.html', context)

def testimonies(request):
    testimony = Testimony.objects.all()
    context = {
        'testimony': testimony
    }
    return render(request, 'testimonies.html', context)

def investment(request):
    context = {
    }
    return render(request, 'investment.html', context)

def adminpage(request):

    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            address_form.save()
            return redirect('adminpage')
    else:
        address_form = AddressForm()

    address = Address.objects.all()
    context = {
        'address_form': address_form,
        'address': address,
    }
    return render(request, 'adminpage.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.method.POST.get('username')
        password = request.method.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('user_login')

def index(request):

    context = {

    }
    return render(request, 'index.html', context)

def signup(request):
    signup = SignupForm

    if request.method == 'POST':
        signup = SignupForm(request.POST)
        if signup.is_valid():
            user = signup.cleaned_data.get('username')
            messages.success(request, 'account was created for' + user)
            signup.save()
            return redirect('user_login')
    context = {
        'signup': signup
    }
    return render(request, 'signup.html', context)

def wallet(request):
    address = Address.objects.all()
    context = {
        'address': address,
    }
    return render(request, 'wallet.html', context)

def alert(request):

    return render(request, 'alert.html')

def user_infor(request, id):
    user_info = Users.objects.get(pk=id)
    if request.method == 'POST':
        bonus=request.POST["bonus"]
        money=request.POST["money"]
        total=request.POST["total"]

        user_info.bonus=bonus
        user_info.money=money
        user_info.total=total
        user_info.save()
        return redirect('users')
    context = {
        'user_info': user_info,
        
    }
    return render(request, 'user_infor.html', context)

def testimony_delete(request, pk):
    testimony = Testimony.objects.get(id=pk)
    if request.method == 'POST':
        testimony.delete()
        return redirect('admintestimony')
    context = {
        'testimony': testimony,
    }
    return render(request, 'testimony_delete.html', context)

def wallet_delete(request, pk):
    wallet = Address.objects.get(id=pk)
    if request.method == 'POST':
        wallet.delete()
        return redirect('adminpage')
    context = {
        'wallet': wallet,
    }
    return render(request, 'wallet_delete.html', context)

def users_delete(request, pk):
    user = Users.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('adminpage')
    context = {
        'user': user,
    }
    return render(request, 'users_delete.html', context)

def users(request):
    user = Users.objects.all()
    context = {
        'user': user
    }
    return render(request, 'users.html', context)


