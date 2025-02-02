from django.urls import path

from .views import StabilizersListView, StabilizersListTipView, StabilizersListTipKorpusView, StabilizerAddView, \
    StabilizerDetailView, StabilizerPrimechChangeView, stabilizer_count, change_stabilizer_amout, \
    datasheet_stabilizer_add, StabilizerEditView, stabilizer_removal_confirmation, stabilizer_delete

urlpatterns = [
    path('', StabilizersListView.as_view(), name='stabilisers_all'),
    path('<int:tipstab_id>/', StabilizersListTipView.as_view(), name='stabilizirs_tip_list'),
    path('<int:tipstab_id>/<int:korpus_id>/', StabilizersListTipKorpusView.as_view(), name='stabilizirs_list_tip_korpus'),
    path('add/', StabilizerAddView.as_view(), name='stabilizer_add'),
    path('detail/<int:pk>/', StabilizerDetailView.as_view(), name='stabilizer_detail'),
    path('edit/<int:pk>/', StabilizerEditView.as_view(), name='stabilizer_edit'),
    path('datasheetadd/', datasheet_stabilizer_add, name='datasheet_stabilizer_add'),
    path('change/<int:pk>/', change_stabilizer_amout, name='change_stabilizer_amout'),
    path('prim/<int:pk>/', StabilizerPrimechChangeView.as_view(), name='stabilizer_primech_change'),
    path('count/<int:pk>/', stabilizer_count, name='stabilizer_count'),
    path('conf/<int:pk>/', stabilizer_removal_confirmation, name='stabilizer_removal_confirmation'),
    path('delete/<int:pk>/', stabilizer_delete, name='stabilizer_delete'),
]