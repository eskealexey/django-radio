from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget
from django.forms import ModelForm, SelectMultiple

from .models import *


class StabilizerAddForm(ModelForm):
    """
    Form for adding transistor
    """
    class Meta:
        model = Stabilizer
        fields = ['name', 'mark', 'tip_stab', 'tip_korpusa', 'volt', 'amount', 'datasheet', 'primech']
        widgets = {
            'datasheet': SelectMultiple(
                attrs={'class': 'form-control', 'rows': 5},
            ),
            'primech': AdminTextareaWidget(attrs={'class': 'form-control', 'rows': 2}),
        }

#
# class DiodeEditForm(ModelForm):
#     """
#     Form for editing transistor
#     """
#     class Meta:
#         model = Diode
#         fields = ['name', 'mark', 'tip_diode', 'tip_korpusa', 'datasheet']
#         widgets = {
#             'datasheet': SelectMultiple(
#                 attrs={'class': 'form-control', 'rows': 5},
#             ),
#         }
#
#
# class DatasheetDiodeAddForm(forms.ModelForm):
#     """
#     Form for adding datasheet
#     """
#     url = forms.FileField(label="Выберите файлы", widget=forms.ClearableFileInput(attrs={'multiple': False}))
#
#     class Meta:
#         model = DatasheetDiode
#         fields = ['discription', 'url']
#
#
# class DiodePrimechAddForm(forms.ModelForm):
#     """
#     Form for adding primech
#     """
#     class Meta:
#         model = Diode
#         fields = ['primech']
#
