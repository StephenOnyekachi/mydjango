
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('home/', views.home, name='home'),
    path('admintestimone/', views.admintestimone, name='admintestimone'),
    path('investment/', views.investment, name='investment'),
    path('testimonies/', views.testimonies, name='testimonies'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('signup/', views.signup, name='signup'),
    path('wallet/', views.wallet, name='wallet'),
    path('users/', views.users, name='users'),
    path('alert/', views.alert, name='alert'),

    path('user_infor/<int:id>/', views.user_infor, name='user_infor'),
    path('users_delete/<int:pk>', views.users_delete, name='users_delete'),
    path('wallet_delete/<int:pk>/', views.wallet_delete, name='wallet_delete'),
    path('testimony_delete/<int:pk>/', views.testimony_delete, name='testimony_delete'),
]
