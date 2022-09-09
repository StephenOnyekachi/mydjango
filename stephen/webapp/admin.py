from django.contrib import admin
from .models import Users, Testimony, Address
# Register your models here.

admin.site.register(Users)
admin.site.register(Testimony)
admin.site.register(Address)