from django.db import models
from django.contrib.auth.models import User
from student.models import STATE_CHOICES
# Create your models here.


YEAR_CHOICES = (
    (1990, 1990),
    (1991, 1991),
    (1992, 1992),
    (1993, 1993),
    (1994, 1994),
    (1995, 1995),
    (1996, 1996),
    (1997, 1997),
    (1998, 1998),
    (1999, 1999),
    (2000, 2000),
    (2001, 2001),
    (2002, 2002),
    (2003, 2003),
    (2004, 2004),
    (2005, 2005),
    (2006, 2006),
    (2007, 2007),
    (2008, 2008),
    (2009, 2009),
    (2010, 2010),
    (2011, 2011),
    (2012, 2012),
    (2013, 2013),
    (2014, 2014),
    (2015, 2015),
    (2016, 2016),
    (2017, 2017),
    (2018, 2018),
    (2019, 2019),
    (2020, 2020),
    (2021, 2021),
    (2022, 2022),
)

STATUS_CHOICES = (
    ("Passed", "Passed"),
    ("Failed", "Failed"),
    ("Pursuing", "Pursuing"),
)

BRANCH_CHOICES = (
    ("Science", "Science"),
    ("Commerce", "Commerce"),
    ("Arts", "Arts"),
)


class Personal_Detail(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    Contact_no = models.CharField(max_length=10)
    Nationality = models.CharField(max_length=100, default="Indian")
    known_languages = models.CharField(max_length=150)


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=150)
    street_name = models.CharField(max_length=150)
    locality = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150, choices=STATE_CHOICES)
    zipcode = models.IntegerField()


class Std_10(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    year_of_passing = models.IntegerField(choices=YEAR_CHOICES)
    board = models.CharField(max_length=100, default="SSC")
    percentage = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=10, default="Passed")


class Std_12(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    year_of_passing = models.IntegerField(choices=YEAR_CHOICES)
    board = models.CharField(max_length=100, default="HSC")
    field = models.CharField(
        max_length=10, choices=BRANCH_CHOICES, default="Science")
    percentage = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=10, default="Passed")


class Year_1(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    year_of_passing = models.IntegerField(
        choices=YEAR_CHOICES)
    board = models.CharField(max_length=100)
    field = models.CharField(max_length=50)
    cgpi = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=10, default="Passed")


class Year_2(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    year_of_passing = models.IntegerField(
        choices=YEAR_CHOICES)
    board = models.CharField(max_length=100)
    field = models.CharField(max_length=50)
    cgpi = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=10, default="Passed")


class Year_3(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    year_of_passing = models.IntegerField(
        choices=YEAR_CHOICES)
    board = models.CharField(max_length=100)
    field = models.CharField(max_length=50)
    cgpi = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=10, default="Passed")


class Year_4(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    year_of_passing = models.IntegerField(
        choices=YEAR_CHOICES)
    board = models.CharField(max_length=100)
    field = models.CharField(max_length=50)
    cgpi = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=10, default="Passed")


class Technical_Skills(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    quick_bio = models.TextField(max_length=1000)
    soft_skills = models.CharField(max_length=300)
    languages_known = models.CharField(max_length=300)
    expert_in = models.CharField(max_length=300)


class Interests(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    professional_interest = models.TextField(max_length=500)
    personal_interest = models.TextField(max_length=500)
    responsibilty = models.TextField(max_length=500)
