# Generated by Django 2.1.2 on 2018-11-17 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20181117_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='donation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
