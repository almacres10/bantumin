# forms.py
from django import forms
from .models import Pegawai, Tiket
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



BANTEK_CHOICES =( 
    ("Pilih Jenis Masalah", "Pilih Jenis Masalah"), 
    ("Software", "Software"), 
    ("Hardware", "Hardware"), 
    ("Jaringan Internet/Intranet", "Jaringan Internet/Intranet"), 
    ("Join Domain", "Join Domain"), 
    ("Permintaan Data", "Permintaan Data"), 
)

BIDANG_CHOICES =( 
    ("Pilih Bidang", "Pilih Bidang"), 
    ("Umum", "Umum"), 
    ("DP3", "DP3"), 
    ("KBP", "KBP"), 
    ("P2 Humas", "P2 Humas"), 
    ("PPIP", "PPIP"),
    ("PEP", "PEP"), 
)


class BantuanTeknisForm(forms.Form):
    nama = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded-md', 'style': 'height: 40px;'}),
        required=True,
        label='Nama',
    )
    bidang = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'border w-80 p-2 rounded-md'}),
        required=True,
        label='Bidang',
        choices=BIDANG_CHOICES,
    )
    jenis_permasalahan = forms.ChoiceField(
        choices=BANTEK_CHOICES,
        label='Jenis Masalah',
        widget=forms.Select(attrs={'class': 'border w-80 p-2 rounded-md'}),
    )
    permasalahan = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'border p-2 rounded-md', 'style': 'height: 100px;'}),
        required=True,
        label='Permasalahan',
    )



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'NIP Bapak/Ibu',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
        
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class TiketForm(forms.ModelForm):
    class Meta:
        model = Tiket
        exclude = ['DATE']