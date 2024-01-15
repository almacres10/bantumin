from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Pegawai, Tiket
from .forms import BantuanTeknisForm, LoginForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




# Create your views here.

def index(request):
    return render(request, "core/index.html")

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Berhasil login.')
                return redirect('core:formBantek')  # Ganti dengan URL redirect yang diinginkan

            else:
                messages.warning(request, 'username atau password Anda salah')
                return redirect('core:login_view')
    else:
        form = LoginForm()

    return render(request, 'core/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        nama = request.POST['nama']
        password = request.POST['password']

        # Buat pengguna baru
        user = User.objects.create_user(username=username, nama=nama, email=email, password=password)
        user.first_name = nama
        user.save()

        # # Otentikasi pengguna dan login setelah registrasi
        # user = authenticate(username=username, password=password)
        # login(request, user)

        return redirect('core:formBantek')

    return render(request, 'core/register.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Berhasil logout.')
    return redirect('core:login_view')


def formBantek(request):
    form = BantuanTeknisForm()
    context = {
        'form': form,
    }

    return render(request, 'core/index.html', context)

def tiketBantek(request):
    if request.method == 'POST':
        form = BantuanTeknisForm(request.POST)

        if form.is_valid():
            nama = form.cleaned_data.get('nama', '')
            bidang = form.cleaned_data.get('bidang', '')
            jenis_masalah = form.cleaned_data.get('jenis_permasalahan', '')
            permasalahan = form.cleaned_data.get('permasalahan', '')

            # Simpan data di model
            tiket = Tiket(NAMA=nama, BIDANG=bidang, JENIS_MASALAH=jenis_masalah, PERMASALAHAN=permasalahan)
            tiket.save()

            return redirect('core:daftarTiket')
        else:
            # Handle the case when the form is not valid
            print(form.errors)  # Print form errors to the console for debugging
    else:
        form = BantuanTeknisForm()

def daftarTiket(request):
    tiket_list = Tiket.objects.all()
    items_per_page = 10
    paginator = Paginator(tiket_list, items_per_page)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'core/tiket.html', {'tiket_list': page_obj})

def deleteTiket(request, tiket_id):
    context = {}
    obj = get_object_or_404(Tiket, ID = tiket_id)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect("/home")
    
    return render(request, "core/hapustiket.html", {'tiket': obj})
