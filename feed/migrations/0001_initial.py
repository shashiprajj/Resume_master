# Generated by Django 3.2.3 on 2021-06-09 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('caption', models.TextField(max_length=300)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
