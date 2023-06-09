from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Civitas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peran_user', models.TextField(blank=True, max_length=100)),
                ('nama', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('civitas_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Civitas')),
                ('ldap_cn', models.TextField(blank=True, max_length=100)),
                ('kd_org', models.TextField(blank=True, max_length=100)),
                ('npm', models.TextField(blank=True, max_length=100)),
                ('faculty', models.TextField(blank=True, max_length=100)),
                ('study_program', models.TextField(blank=True, max_length=100)),
                ('educational_program', models.TextField(blank=True, max_length=100)),
            ],
            bases=('api.civitas',),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('civitas_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Civitas')),
                ('nip', models.TextField(blank=True, max_length=100)),
            ],
            bases=('api.civitas',),
        ),
        migrations.AddField(
            model_name='civitas',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

