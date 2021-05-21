from django import forms
from .models import car, spare, engine
from django.forms import ModelForm

class Formulario(forms.Form):
    search=forms.CharField(label="", required=False,widget=forms.TextInput(attrs={"placeholder":"Search for spare part code..."}))

# class sideFilter(forms.Form):
#     select=forms.ModelChoiceField(queryset=car.objects.all(),
#     label="Manufacturer",
#     )
#     print(type(select))

# class sideFilter(forms.ModelForm):
#     class Meta:
#         model=car
#         fields=['car_manufacturer']
#         labels={"car_manufacturer":"fabricante",}
#     widgets={
#         "car_manufacturer": forms.NullBooleanSelect
#     }

class listCars(forms.Form):
    select=forms.ModelChoiceField(queryset=car.objects.all(),
    # label="Manufacturer",
    # widget=forms.Select
    )