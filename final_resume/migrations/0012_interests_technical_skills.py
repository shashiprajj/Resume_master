# Generated by Django 3.2.3 on 2021-06-15 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('final_resume', '0011_alter_address_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technical_Skills',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quick_bio', models.TextField(max_length=1000)),
                ('soft_skills', models.CharField(max_length=300)),
                ('languages_known', models.CharField(max_length=300)),
                ('expert_in', models.CharField(max_length=300)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('professional_interest', models.TextField(max_length=500)),
                ('personal_interest', models.TextField(max_length=500)),
                ('responsibilty', models.TextField(max_length=500)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
