# Generated by Django 3.2.3 on 2021-05-30 09:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_poem_poem_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_platform', models.CharField(choices=[('COURSERA', 'Coursera'), ('UDEMY', 'Udemy'), ('EDX', 'Edx'), ('OTHERS', 'Others')], max_length=8)),
                ('course_img', models.ImageField(upload_to='certificates')),
                ('date_completed', models.DateField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('course_description', models.TextField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
