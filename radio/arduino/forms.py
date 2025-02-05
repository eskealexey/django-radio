from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget
from django.forms import ModelForm, SelectMultiple

from .models import *


class DatasheetModulAddForm(forms.ModelForm):
    """
    Form for adding datasheet
    """
    url = forms.FileField(label="Выберите файлы", widget=forms.ClearableFileInput(attrs={'multiple': False}))

    class Meta:
        model = DatasheetModul
        fields = ['discription', 'url']


class ModulAddForm(ModelForm):
    """
    Form for adding MCU
    """
    class Meta:
        model = Modul
        fields = ['name', 'mark', 'tip_modul', 'naznachenie' , 'amount', 'datasheet', 'primech']
        widgets = {
            'datasheet': SelectMultiple(
                attrs={'class': 'form-control', 'rows': 5},
            ),
            'primech': AdminTextareaWidget(attrs={'class': 'form-control', 'rows': 2}),
        }


class ModulEditForm(ModelForm):
    """
    Form for editing MCU
    """
    class Meta:
        model = Modul
        fields = ['name', 'mark', 'tip_modul', 'naznachenie', 'datasheet']
        widgets = {
            'datasheet': SelectMultiple(
                attrs={'class': 'form-control', 'rows': 5},
            ),
        }


class ModulPrimechAddForm(forms.ModelForm):
    """
    Form for adding primech
    """
    class Meta:
        model = Modul
        fields = ['primech']
