from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget, FilteredSelectMultiple
from django.forms import ModelForm, Textarea, SplitDateTimeWidget, CheckboxSelectMultiple, SelectMultiple, FileInput

from .models import *

class TransistorAddForm(ModelForm):
    """
    Form for adding transistor
    """
    class Meta:
        model = Transistor
        fields = ['name', 'mark', 'tip_trans', 'tip_korpusa', 'amount', 'status', 'datasheet', 'primech']
        widgets = {
            'datasheet': SelectMultiple(
                attrs={'class': 'form-control', 'rows': 5},
                # verbose_name='Datasheets',
                # is_stacked=False
            ),
            'primech': AdminTextareaWidget(attrs={'class': 'form-control', 'rows': 2}),
        }

class DatasheetTransistorAddForm(forms.ModelForm):
    class Meta:
        model = DatasheetTransistor
        fields = ['discription', 'url']
