# Generated by Django 3.2.3 on 2021-06-18 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_project_date_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_image', models.ImageField(blank=True, null=True, upload_to='project_image/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
