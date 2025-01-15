from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Transistor)
admin.site.register(TipTrans)
admin.site.register(TipKorpus)
admin.site.register(DatasheetTransistor)