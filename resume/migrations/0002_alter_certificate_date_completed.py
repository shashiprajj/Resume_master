# Generated by Django 3.2.3 on 2021-06-13 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='date_completed',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
