from django import forms
from .models import Std_10, Std_12, Year_1, Year_2, Year_3, Year_4, Personal_Detail, Address, Technical_Skills, Interests


class PersonalDetailForm(forms.ModelForm):
    class Meta:
        model = Personal_Detail
        fields = ["Contact_no", "Nationality", "known_languages"]


class PersonalDetailUpdateForm(forms.ModelForm):
    class Meta:
        model = Personal_Detail
        fields = ["Contact_no", "Nationality", "known_languages"]


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["room_no", "street_name",
                  "locality", "city", "state", "zipcode"]


class AddressUpdateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["room_no", "street_name",
                  "locality", "city", "state", "zipcode"]


class Std_10Form(forms.ModelForm):
    class Meta:
        model = Std_10
        fields = ["year_of_passing", "board", "percentage", "status"]


class Std_10UpdateForm(forms.ModelForm):
    class Meta:
        model = Std_10
        fields = ["year_of_passing", "board", "percentage", "status"]


class Std_12Form(forms.ModelForm):
    class Meta:
        model = Std_12
        fields = ["year_of_passing", "board", "field", "percentage", "status"]


class Std_12UpdateForm(forms.ModelForm):
    class Meta:
        model = Std_12
        fields = ["year_of_passing", "board", "percentage", "status"]


class First_YearForm(forms.ModelForm):
    class Meta:
        model = Year_1
        fields = ["year_of_passing", "board", "field", "cgpi", "status"]


class First_YearUpdateForm(forms.ModelForm):
    class Meta:
        model = Year_1
        fields = ["year_of_passing", "board", "field", "cgpi", "status"]


class Second_YearForm(forms.ModelForm):
    class Meta:
        model = Year_2
        fields = ["year_of_passing", "board", "field", "cgpi", "status"]


class Second_YearUpdateForm(forms.ModelForm):
    class Meta:
        model = Year_2
        fields = ["year_of_passing", "board", "field", "cgpi", "status"]


class Third_YearForm(forms.ModelForm):
    class Meta:
        model = Year_3
        fields = ["year_of_passing", "board", "field", "cgpi", "status"]


class Third_YearUpdateForm(forms.ModelForm):
    class Meta:
        model = Year_3
        fields = ["year_of_passing", "board", "field", "cgpi", "status"]


class Fourth_YearForm(forms.ModelForm):
    class Meta:
        model = Year_4
        fields = ["year_of_passing", "board", "field", "cgpi", "status"]


class Fourth_YearUpdateForm(forms.ModelForm):
    class Meta:
        model = Year_4
        fields = ["year_of_passing", "board", "field", "cgpi", "status"]


class TechnicalSkillsForm(forms.ModelForm):
    class Meta:
        model = Technical_Skills
        fields = ["quick_bio", "soft_skills", "languages_known", "expert_in"]


class TechnicalSkillsUpdateForm(forms.ModelForm):
    class Meta:
        model = Technical_Skills
        fields = ["quick_bio", "soft_skills", "languages_known", "expert_in"]


class InterestsForm(forms.ModelForm):
    class Meta:
        model = Interests
        fields = ["professional_interest",
                  "personal_interest", "responsibilty"]


class InterestsUpdateForm(forms.ModelForm):
    class Meta:
        model = Interests
        fields = ["professional_interest",
                  "personal_interest", "responsibilty"]
