from django.forms import ModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your models here.

# from .forms import ModelForm

from .models import Users
from .models import Testimony
from .models import Address

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'


class TestimonyForm(ModelForm):
    class Meta:
        model = Testimony
        fields = '__all__'


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'