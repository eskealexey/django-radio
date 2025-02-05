from django.urls import path


from .views import moduls_all, moduls_tip_list, moduls_nazn_list

urlpatterns = [
    path('', moduls_all, name='moduls_all'),
    path('<int:pk>/', moduls_tip_list, name='moduls_tip_list'),
    path('<int:pk>/', moduls_nazn_list, name='moduls_nazn_list'),
    # path('add/', mcu_add, name='mcu_add'),
    # path('detail/<int:pk>/', mcu_detail, name='mcu_detail'),
    # path('edit/<int:pk>/', mcu_edit, name='mcu_edit'),
    # path('datasheetadd/', datasheet_mcu_add, name='datasheet_mcu_add'),
    # path('prim/<int:pk>/', mcu_primech_change, name='mcu_primech_change'),
    # path('count/<int:pk>/', mcu_count, name='mcu_count'),
    # path('conf/<int:pk>/', mcu_removal_confirmation, name='mcu_removal_confirmation'),
    # path('delete/<int:pk>/', mcu_delete, name='mcu_delete'),
]