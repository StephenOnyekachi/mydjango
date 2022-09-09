from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Testimony
from .models import Address
from .models import Users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import TestimonyForm
from .forms import AddressForm
from .forms import SignupForm
from .forms import UsersForm

# Create your views here.

@login_required(login_url='user_login')
def home(request):
    user = request.user
    if request.method == 'POST':
        bonus = int(request.POST["bonus"])
        money = int(request.POST["money"])
        total = int(request.POST["bonus"]) + int(request.POST["money"])
        percentage = int(request.POST["money"]) / 20

        user.bonus = bonus
        user.money = money
        user.total = total
        user.percentage = percentage
        user.save()
        return redirect('users')
    address = Address.objects.all()
    context = {
        'address': address,
     
    }
    return render(request, 'home.html', context)

def index(request):
    context = {

    }
    return render(request, 'index.html', context)

@login_required(login_url='user_login')
def admintestimone(request):
    if request.method == 'POST':
        image = request.FILES.get("image")
        content = request.POST['content']
        link = request.POST['link']
        Testimony.objects.create(image=image, content=content, link=link)
    else:
        add_testimony = Testimony()

    testimony = Testimony.objects.all()
    context = {
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

@login_required(login_url='user_login')
def adminpage(request):
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            address_form.save()
            return redirect('adminpage')
    else:
        address = AddressForm()

    all_address = Address.objects.all()
    context = {
        'all_address': all_address,
        'address': address,
    }
    return render(request, 'adminpage.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('adminpage')
            else:
                login(request, user)
                return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('user_login')

def signup(request):
    signup = SignupForm
    if request.method == 'POST':
        signup = SignupForm(request.POST)
        if signup.is_valid():
            user = signup.cleaned_data.get('username')
            messages.success(request, 'account was created for ' + user)
            signup.save()
            return redirect('user_login')
    context = {
        'signup': signup
    }
    return render(request, 'signup.html', context)

@login_required(login_url='user_login')
def wallet(request):
    user = request.user
    if request.method == 'POST':
        bonus = int(request.POST["bonus"])
        money = int(request.POST["money"])
        total = int(request.POST["bonus"]) + int(request.POST["money"])

        user.bonus = bonus
        user.money = money
        user.total = total
        user.save()
        return redirect('users')
    context = {
        'user': user,

    }
    return render(request, 'wallet.html', context)

@login_required(login_url='user_login')
def alert(request):

    return render(request, 'alert.html')

@login_required(login_url='user_login')
def testimony_delete(request, pk):
    testimony = Testimony.objects.get(id=pk)
    if request.method == 'POST':
        testimony.delete()
        return redirect('admintestimone')
    context = {
        'testimony': testimony,
    }
    return render(request, 'testimony_delete.html', context)

@login_required(login_url='user_login')
def wallet_delete(request, pk):
    wallet = Address.objects.get(id=pk)
    if request.method == 'POST':
        wallet.delete()
        return redirect('adminpage')
    context = {
        'wallet': wallet,
    }
    return render(request, 'wallet_delete.html', context)

@login_required(login_url='user_login')
def user_infor(request, pk):
    user_info = Users.objects.get(id=pk)
    if request.method == 'POST':
        bonus = int(request.POST["bonus"])
        money = int(request.POST["money"])
        total = int(request.POST["bonus"]) + int(request.POST["money"])

        user_info.bonus = bonus
        user_info.money = money
        user_info.total = total
        user_info.save()
        return redirect('users')
    context = {
        'user_info': user_info,

    }
    return render(request, 'user_infor.html', context)

@login_required(login_url='user_login')
def users_delete(request, pk):
    user = Users.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    context = {
        'user': user,
    }
    return render(request, 'users_delete.html', context)

@login_required(login_url='user_login')
def users(request):
    # user = User.objects.filter(is_superuser=False)
    user = Users.objects.all()
    context = {
        'user': user
    }
    return render(request, 'users.html', context)

@login_required(login_url='user_login')
def new_users(request):
    if request.method == 'POST':
        users = UsersForm(request.POST)
        if users.is_valid():
            users.save()
            return redirect('users')
    new_user = User.objects.filter(is_superuser=False)
    context = {
        'new_user': new_user,
        'users': users,
    }

    return render(request, 'new_users.html', context)


