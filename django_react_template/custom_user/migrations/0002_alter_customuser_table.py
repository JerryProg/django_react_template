# Generated by Django 4.2.7 on 2023-11-23 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customuser',
            table='users',
        ),
    ]
