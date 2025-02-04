from django.contrib import admin

from .models import Mcu, TipMcu, TipKorpusMcu, DatasheetMcu

# Register your models here.
admin.site.register(Mcu)
admin.site.register(TipMcu)
admin.site.register(TipKorpusMcu)
admin.site.register(DatasheetMcu)