# Generated by Django 2.0.2 on 2018-03-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_mahasiswa_tingkatkerjasama'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosen',
            name='id',
        ),
        migrations.RemoveField(
            model_name='mahasiswa',
            name='id',
        ),
        migrations.RemoveField(
            model_name='matakuliah',
            name='id',
        ),
        migrations.AlterField(
            model_name='dosen',
            name='nip_pengajar',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='npm',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='matakuliah',
            name='kode_matkul',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
