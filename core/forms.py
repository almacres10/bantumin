# forms.py
from django import forms
from .models import Pegawai
from django.contrib.auth.forms import AuthenticationForm



BANTEK_CHOICES =( 
    ("0", "Pilih Jenis Masalah"), 
    ("1", "Software"), 
    ("2", "Hardware"), 
    ("3", "Jaringan Internet/Intranet"), 
    ("4", "Join Domain"), 
    ("5", "Permintaan Data"), 
)

class BantuanTeknisForm(forms.Form):
    nama_field = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded-md'}),
        required=True,
    )
    bidang_field = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded-md'}),
        required=True,
    )
    jenis_permasalahan = forms.ChoiceField(
        choices= BANTEK_CHOICES,
        label='Jenis Masalah',
        widget=forms.Select(attrs={'class': 'border w-80 p-2 rounded-md'}),
    )
    permasalahan = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'border p-2 rounded-md'}),
        required=True,
    )


class LoginForm(AuthenticationForm):
    nip_pendek = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'NIP Bapak/Ibu',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
        
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))