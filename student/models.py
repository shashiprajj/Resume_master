from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone, tree


# Create your models here.
STATE_CHOICES = (
    ('Select', 'Select'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('West Bengal', 'West Bengal'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Orissa', 'Orissa'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
)


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    full_name = models.CharField(max_length=100, default="None")
    college = models.CharField(max_length=200, default="None")
    city = models.CharField(max_length=50, default="None")
    state = models.CharField(choices=STATE_CHOICES,
                             max_length=50, default="None")

    def __str__(self):
        return f'{self.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
