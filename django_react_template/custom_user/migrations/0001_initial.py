# Generated by Django 4.2.7 on 2023-11-23 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Usuario')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de ingreso')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Ultimo acceso')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]