from django.urls import path
from . import views 

app_name = 'core'

urlpatterns = [
    path('home/', views.formBantek, name='formBantek'),
    path('tiket/', views.tiketBantek, name='tiketBantek'),
    path('tiket/daftar/', views.daftarTiket, name='daftarTiket'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='user_logout'),
    path('delete/tiket/<int:tiket_id>/', views.deleteTiket, name='deleteTiket')
]
