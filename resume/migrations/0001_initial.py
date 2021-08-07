# Generated by Django 3.2.3 on 2021-06-04 21:01

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
            name='Certificate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
                ('course_platform', models.CharField(choices=[('COURSERA', 'Coursera'), ('UDEMY', 'Udemy'), ('EDX', 'Edx'), ('OTHERS', 'Others')], max_length=8)),
                ('course_img', models.ImageField(upload_to='certificates')),
                ('date_completed', models.DateField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('course_description', models.TextField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]