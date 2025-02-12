from django.urls import path
from .views import transistors_all, transistors_list_tip, transistors_list_tip_korpus, datasheet_add, transistor_count, \
    transistor_edit, transistor_delete, transistor_removal_confirmation
from .views import transistor_add, change_transistor_amout, transistor_detail, transistor_primech_change           #, datasheet_add


urlpatterns = [
    path('', transistors_all, name='transistors_all'),
    path('<int:tiptrans_id>/', transistors_list_tip, name='transistors_tip_list'),
    path('<int:tiptrans_id>/<int:korpus_id>', transistors_list_tip_korpus, name='transistors_list_tip_korpus'),
    path('add/', transistor_add, name='transistor_add'),
    path('edit/<int:pk>/', transistor_edit, name='transistor_edit'),
    path('datasheetadd/', datasheet_add, name='datasheet_trahsisitor_add'),
    path('change/<int:transistor_id>/', change_transistor_amout, name='change_transistor_amout'),
    path('detail/<int:pk>/', transistor_detail, name='transistor_detail'),
    path('prim/<int:transistor_id>/', transistor_primech_change, name='transistor_primech_change'),
    path('count/<int:transistor_id>/', transistor_count, name='transistor_count'),
    path('conf/<int:pk>/', transistor_removal_confirmation, name='transistor_removal_confirmation'),
    path('delete/<int:pk>/', transistor_delete, name='transistor_delete'),
]