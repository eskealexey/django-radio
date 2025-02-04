from django.urls import path

from .views import mcu_all, mcu_tip_list, mcu_tip_korpus_list, datasheet_mcu_add, mcu_add, mcu_detail, \
    mcu_edit, mcu_primech_change, mcu_count, mcu_removal_confirmation, mcu_delete


urlpatterns = [
    path('', mcu_all, name='mcu_all'),
    path('<int:tipmcu_id>/', mcu_tip_list, name='mcu_tip_list'),
    path('<int:tipmcu_id>/<int:korpus_id>/', mcu_tip_korpus_list, name='mcu_tip_korpus_list'),
    path('add/', mcu_add, name='mcu_add'),
    path('detail/<int:pk>/', mcu_detail, name='mcu_detail'),
    path('edit/<int:pk>/', mcu_edit, name='mcu_edit'),
    path('datasheetadd/', datasheet_mcu_add, name='datasheet_mcu_add'),
    path('prim/<int:pk>/', mcu_primech_change, name='mcu_primech_change'),
    path('count/<int:pk>/', mcu_count, name='mcu_count'),
    path('conf/<int:pk>/', mcu_removal_confirmation, name='mcu_removal_confirmation'),
    path('delete/<int:pk>/', mcu_delete, name='mcu_delete'),
]