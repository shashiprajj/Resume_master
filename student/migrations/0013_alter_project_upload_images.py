# Generated by Django 3.2.3 on 2021-05-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_alter_project_upload_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='upload_images',
            field=models.FileField(blank=True, null=True, upload_to='projects'),
        ),
    ]
