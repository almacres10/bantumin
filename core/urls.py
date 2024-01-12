from django.urls import path
from . import views 

app_name = 'core'

urlpatterns = [
    path('home/', views.formBantek, name='formBantek'),
    path('', views.login_view, name='login_view'),
    path('tiket/', views.tiketBantek, name='tiketBantek'),
    path('tiket/daftar/', views.daftarTiket, name='daftarTiket'),
    path('register/', views.register, name='register')
]
