from django.contrib import admin

from .models import Transistor
from .forms import TransistorAddForm

class DatasheetAdmin(admin.ModelAdmin):
    form = TransistorAddForm  # Указываем свою форму
    list_display = ('name', 'mark', 'tip_trans', 'tip_korpusa', 'amount', 'status')
    search_fields = ('name', 'mark')


class TransistorAdmin:
    pass


admin.site.register(Transistor)



# Register your models here.
from .models import *





# admin.site.register(Transistor)
admin.site.register(TipTrans)
admin.site.register(TipKorpus)
admin.site.register(DatasheetTransistor)