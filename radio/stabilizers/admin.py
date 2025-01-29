from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(TipStabilizer)
admin.site.register(TipKorpusStabilizer)
admin.site.register(DatasheetStabilizer)
admin.site.register(Stabilizer)