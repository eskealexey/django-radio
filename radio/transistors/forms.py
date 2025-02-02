from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget
from django.forms import ModelForm, SelectMultiple

from .models import *


class TransistorAddForm(ModelForm):
    """
    Form for adding transistor
    """
    class Meta:
        model = Transistor
        fields = ['name', 'mark', 'tip_trans', 'tip_korpusa', 'amount', 'datasheet', 'primech']
        widgets = {
            'datasheet': SelectMultiple(
                attrs={'class': 'form-control', 'rows': 5},
            ),
            'primech': AdminTextareaWidget(attrs={'class': 'form-control', 'rows': 2}),
        }


class TransistorEditForm(ModelForm):
    """
    Form for editing transistor
    """
    class Meta:
        model = Transistor
        fields = ['name', 'mark', 'tip_trans', 'tip_korpusa', 'datasheet']
        widgets = {
            'datasheet': SelectMultiple(
                attrs={'class': 'form-control', 'rows': 5},
            ),
        }


class DatasheetTransistorAddForm(forms.ModelForm):
    """
    Form for adding datasheet
    """
    url = forms.FileField(label="Выберите файлы", widget=forms.ClearableFileInput(attrs={'multiple': False}))

    class Meta:
        model = DatasheetTransistor
        fields = ['discription', 'url']


class TransistorPrimechAddForm(forms.ModelForm):
    """
    Form for adding primech
    """
    class Meta:
        model = Transistor
        fields = ['primech']

