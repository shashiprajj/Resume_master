# Generated by Django 3.2.3 on 2021-06-18 12:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210618_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
