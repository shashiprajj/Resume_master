# Generated by Django 3.2.3 on 2021-06-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_resume', '0012_interests_technical_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_detail',
            name='Contact_no',
            field=models.CharField(max_length=10),
        ),
    ]
