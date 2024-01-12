from django.db import models

# Create your models here.

class Pegawai(models.Model):
    id_pegawai = models.AutoField(primary_key=True, null=False)
    NAMA = models.CharField(max_length=255, null=True)
    NIP = models.CharField(max_length=255, null=True)
    IP = models.CharField(max_length=255, null=True)
    JABATAN = models.FloatField(null=True)
    BIDANG = models.CharField(max_length=255, null=True)
    

class Tiket(models.Model):
    ID = models.AutoField(primary_key=True)
    NAMA = models.CharField(max_length=255, null=False)
    BIDANG = models.CharField(max_length=255, null=False)
    JENIS_MASALAH = models.CharField(max_length=255, null=False)
    PERMASALAHAN = models.TextField(null=False)
    DATE = models.DateTimeField(auto_now_add=True)
