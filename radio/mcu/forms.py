from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget
from django.forms import ModelForm, SelectMultiple

from .models import *


class McuAddForm(ModelForm):
    """
    Form for adding MCU
    """
    class Meta:
        model = Mcu
        fields = ['name', 'mark', 'tip_mcu', 'tip_korpusa', 'amount', 'datasheet', 'primech']
        widgets = {
            'datasheet': SelectMultiple(
                attrs={'class': 'form-control', 'rows': 5},
            ),
            'primech': AdminTextareaWidget(attrs={'class': 'form-control', 'rows': 2}),
        }


class McuEditForm(ModelForm):
    """
    Form for editing MCU
    """
    class Meta:
        model = Mcu
        fields = ['name', 'mark', 'tip_mcu', 'tip_korpusa', 'datasheet']
        widgets = {
            'datasheet': SelectMultiple(
                attrs={'class': 'form-control', 'rows': 5},
            ),
        }


class DatasheetMcuAddForm(forms.ModelForm):
    """
    Form for adding datasheet
    """
    url = forms.FileField(label="Выберите файлы", widget=forms.ClearableFileInput(attrs={'multiple': False}))

    class Meta:
        model = DatasheetMcu
        fields = ['discription', 'url']


class McuPrimechAddForm(forms.ModelForm):
    """
    Form for adding primech
    """
    class Meta:
        model = Mcu
        fields = ['primech']

