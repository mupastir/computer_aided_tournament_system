from django import forms
from django.forms import DateInput
from django_countries.widgets import CountrySelectWidget
from user_auth.models import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['birthdate',
                  'first_name',
                  'last_name',
                  'gender',
                  'country']
        widgets = {'country': CountrySelectWidget(),
                   'birthdate': DateInput()}
