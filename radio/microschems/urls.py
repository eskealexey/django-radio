from django.urls import path

from .views import microschems_all, microschems_tip_list, microschems_tip_korpus_list, microschems_nazn_list, \
    datasheet_add, microschema_add, microschema_detail, microschema_edit, microschema_primech_change, microschema_count, \
    microschema_removal_confirmation, microschema_delete

urlpatterns = [
    path('', microschems_all, name='microschems_all'),
    path('<int:tip_id>/', microschems_tip_list, name='microschems_tip_list'),
    path('<int:tip_id>/<int:korpus_id>/', microschems_tip_korpus_list, name='microschems_tip_korpus_list'),
    path('nazn/<int:nazn_id>/', microschems_nazn_list, name='microschems_nazn_list'),
    path('datasheetadd/', datasheet_add, name='datasheet_microschema_add'),
    path('add/', microschema_add, name='microschema_add'),
    path('detail/<int:pk>/', microschema_detail, name='microschema_detail'),
    path('edit/<int:pk>/', microschema_edit, name='microschema_edit'),
    path('prim/<int:microschema_id>/', microschema_primech_change, name='microschema_primech_change'),
    path('count/<int:microschema_id>/', microschema_count, name='microschema_count'),
    path('conf/<int:pk>/', microschema_removal_confirmation, name='microschema_removal_confirmation'),
    path('delete/<int:pk>/', microschema_delete, name='microschema_delete'),
]