# Generated by Django 3.2.3 on 2021-05-30 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20210530_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='poem_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='poem',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]