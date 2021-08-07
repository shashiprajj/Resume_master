from django.contrib import admin
from .models import Std_10, Std_12, Year_1, Year_2, Year_3, Year_4, Personal_Detail, Address, Technical_Skills, Interests
# Register your models here.


@admin.register(Personal_Detail)
class Personal_DetailAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "Contact_no",
                    "Nationality", "known_languages"]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["username", "room_no", "street_name",
                    "locality", "city", "state", "zipcode"]


@admin.register(Std_10)
class Std_10Admin(admin.ModelAdmin):
    list_display = ["id", "username", "year_of_passing",
                    "board", "percentage", "status"]


@admin.register(Std_12)
class Std_12Admin(admin.ModelAdmin):
    list_display = ["username", "year_of_passing",
                    "board", "field", "percentage", "status"]


@admin.register(Year_1)
class First_YearAdmin(admin.ModelAdmin):
    list_display = ["username", "year_of_passing",
                    "board", "field", "cgpi", "status"]


@admin.register(Year_2)
class Second_YearAdmin(admin.ModelAdmin):
    list_display = ["username", "year_of_passing",
                    "board", "field", "cgpi", "status"]


@admin.register(Year_3)
class Third_YearAdmin(admin.ModelAdmin):
    list_display = ["username", "year_of_passing",
                    "board", "field", "cgpi", "status"]


@admin.register(Year_4)
class Fourth_YearAdmin(admin.ModelAdmin):
    list_display = ["username", "year_of_passing",
                    "board", "field", "cgpi", "status"]


@admin.register(Technical_Skills)
class TechnicalSkilsAdmin(admin.ModelAdmin):
    list_display = ["username", "soft_skills",
                    "languages_known", "expert_in"]


@admin.register(Interests)
class InterestsAdmin(admin.ModelAdmin):
    list_display = ["username", "professional_interest",
                    "personal_interest", "responsibilty"]
