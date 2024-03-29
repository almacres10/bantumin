# Generated by Django 5.0 on 2024-01-01 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pegawai',
            fields=[
                ('id_pegawai', models.AutoField(primary_key=True, serialize=False)),
                ('NAMA', models.CharField(max_length=255, null=True)),
                ('NIP', models.CharField(max_length=255, null=True)),
                ('IP', models.CharField(max_length=255, null=True)),
                ('JABATAN', models.FloatField(null=True)),
                ('BIDANG', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tiket',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('NAMA', models.CharField(max_length=255)),
                ('BIDANG', models.CharField(max_length=255)),
                ('JENIS_MASALAH', models.CharField(max_length=255)),
                ('PERMASALAHAN', models.TextField()),
                ('DATE', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
