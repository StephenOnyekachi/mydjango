from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    name                = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_joined         = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name="last login", auto_now=True)
    total               = models.IntegerField(null=True)
    bonus               = models.IntegerField(null=True)
    money               = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Testimony(models.Model):
    content             = models.TextField(max_length=1000, null=True)
    image               = models.ImageField(upload_to='pics', null=True)
    link                = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.link


class Address(models.Model):
    address_name        = models.CharField(max_length=1000)
    address_link        = models.CharField(max_length=1000)

    def __str__(self):
        return self.address_name
