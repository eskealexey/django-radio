from django.urls import path
from .views import transistors_all, transistors_list_tip, transistors_list_tip_korpus, datasheet_add
from .views import transistor_add, change_transistor_amout           #, datasheet_add


urlpatterns = [
    path('', transistors_all, name='transistors_all'),
    path('<int:tiptrans_id>/', transistors_list_tip, name='transistors_tip_list'),
    path('<int:tiptrans_id>/<int:korpus_id>', transistors_list_tip_korpus, name='transistors_list_tip_korpus'),
    path('add/', transistor_add, name='transistor_add'),
    path('datasheetadd/', datasheet_add, name='datasheet_add'),
    path('change/<int:transistor_id>/', change_transistor_amout, name='change_transistor_amout'),
]