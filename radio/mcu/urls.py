from django.urls import path

from .views import mcu_all, mcu_tip_list

urlpatterns = [
    path('', mcu_all, name='mcu_all'),
    path('<int:tipmcu_id>/', mcu_tip_list, name='mcu_tip_list'),
    # path('<int:tip_id>/<int:korpus_id>/', DiodeListTipKorpusView.as_view(), name='diodes_list_tip_korpus'),
    # path('add/', DiodeAddView.as_view(), name='diode_add'),
    # path('detail/<int:pk>/', DiodeDetailView.as_view(), name='diode_detail'),
    # path('edit/<int:pk>/', DiodeEditView.as_view(), name='diode_edit'),
    # path('datasheetadd/', datasheet_diode_add, name='datasheet_diode_add'),
    # path('change/<int:pk>/', change_diode_amout, name='change_diode_amout'),
    # path('prim/<int:pk>/', DiodePrimechChangeView.as_view(), name='diode_primech_change'),
    # path('count/<int:pk>/', diode_count, name='diode_count'),
    # path('conf/<int:pk>/', diode_removal_confirmation, name='diode_removal_confirmation'),
    # path('delete/<int:pk>/', diode_delete, name='diode_delete'),
]