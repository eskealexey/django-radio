from django.urls import path

from .views import DiodeListView, DiodeListTipView, DiodeListTipKorpusView, DiodeAddView, \
    DiodeDetailView, DiodeEditView, DiodePrimechChangeView

urlpatterns = [
    path('', DiodeListView.as_view(), name='diodes_all'),
    path('<int:tipdiode_id>/', DiodeListTipView.as_view(), name='diodes_tip_list'),
    path('<int:tip_id>/<int:korpus_id>/', DiodeListTipKorpusView.as_view(), name='diodes_list_tip_korpus'),
    path('add/', DiodeAddView.as_view(), name='diode_add'),
    path('detail/<int:pk>/', DiodeDetailView.as_view(), name='diode_detail'),
    path('edit/<int:pk>/', DiodeEditView.as_view(), name='diode_edit'),
    # path('datasheetadd/', datasheet_add, name='datasheet_trahsisitor_add'),
    # path('change/<int:transistor_id>/', change_transistor_amout, name='change_transistor_amout'),
    path('prim/<int:pk>/', DiodePrimechChangeView.as_view(), name='diode_primech_change'),
    # path('count/<int:transistor_id>/', transistor_count, name='transistor_count'),
    # path('conf/<int:pk>/', transistor_removal_confirmation, name='transistor_removal_confirmation'),
    # path('delete/<int:pk>/', transistor_delete, name='transistor_delete'),
]