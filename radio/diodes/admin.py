from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Diode)
admin.site.register(TipDiode)
admin.site.register(TipKorpusDiode)
admin.site.register(DatasheetDiode)