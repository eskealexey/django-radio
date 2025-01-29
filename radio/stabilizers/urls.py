from django.urls import path

from .views import StabilizersListView, StabilizersListTipView, StabilizersListTipKorpusView, StabilizerAddView, \
    StabilizerDetailView

urlpatterns = [
    path('', StabilizersListView.as_view(), name='stabilisers_all'),
    path('<int:tipstab_id>/', StabilizersListTipView.as_view(), name='stabilizirs_tip_list'),
    path('<int:tipstab_id>/<int:korpus_id>/', StabilizersListTipKorpusView.as_view(), name='stabilizirs_list_tip_korpus'),
    path('add/', StabilizerAddView.as_view(), name='stabilizer_add'),
    path('detail/<int:pk>/', StabilizerDetailView.as_view(), name='stabilizer_detail'),
    # path('edit/<int:pk>/', DiodeEditView.as_view(), name='diode_edit'),
    # path('datasheetadd/', DatasheetDiodeAddView.as_view(), name='datasheet_diode_add'),
    # path('change/<int:pk>/', change_diode_amout, name='change_diode_amout'),
    # path('prim/<int:pk>/', DiodePrimechChangeView.as_view(), name='diode_primech_change'),
    # path('count/<int:pk>/', diode_count, name='diode_count'),
    # path('conf/<int:pk>/', diode_removal_confirmation, name='diode_removal_confirmation'),
    # path('delete/<int:pk>/', diode_delete, name='diode_delete'),
]