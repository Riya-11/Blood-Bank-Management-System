# Generated by Django 2.1 on 2018-11-16 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='wallet',
        ),
    ]