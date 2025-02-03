from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget
from django.forms import ModelForm, SelectMultiple

from .models import *


class MicroschemaAddForm(ModelForm):
    """
    Form for adding Microschema
    """
    class Meta:
        model = Microschema
        fields = ['name', 'mark', 'tip_micro', 'tip_korpusa', 'naznachenie', 'amount', 'datasheet', 'primech']
        widgets = {
            'datasheet': SelectMultiple(
                attrs={'class': 'form-control', 'rows': 5},
            ),
            'primech': AdminTextareaWidget(attrs={'class': 'form-control', 'rows': 2}),
        }


class MicroschemaEditForm(ModelForm):
    """
    Form for editing microschema
    """
    class Meta:
        model = Microschema
        fields = ['name', 'mark', 'tip_micro', 'tip_korpusa', 'naznachenie', 'datasheet']
        widgets = {
            'datasheet': SelectMultiple(
                attrs={'class': 'form-control', 'rows': 5},
            ),
        }


class DatasheetMicroschemaAddForm(forms.ModelForm):
    """
    Form for adding datasheet
    """
    url = forms.FileField(label="Выберите файлы", widget=forms.ClearableFileInput(attrs={'multiple': False}))

    class Meta:
        model = DatasheetMicroschema
        fields = ['discription', 'url']


class MicroschemaPrimechAddForm(forms.ModelForm):
    """
    Form for adding primech
    """
    class Meta:
        model = Microschema
        fields = ['primech']

