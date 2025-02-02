from django.urls import path

from .views import microschems_all
urlpatterns = [
    path('', microschems_all, name='microschems_all'),
    # path('<int:tip_id>/', microschems_list_tip, name='microschems_list_tip'),
    #
    # path('<int:tip_id>/<int:korpus_id>/', microschems_list_tip_korpus, name='microschems_list_tip_korpus'),

    # path('<int:tip_id>/<int:korpus_id>', microschems_list_tip_korpus, name='microschems_list_tip_korpus'),
#     path('add/', transistor_add, name='transistor_add'),
#     path('edit/<int:pk>/', transistor_edit, name='transistor_edit'),
#     path('datasheetadd/', datasheet_add, name='datasheet_trahsisitor_add'),
#     path('change/<int:transistor_id>/', change_transistor_amout, name='change_transistor_amout'),
#     path('detail/<int:pk>/', transistor_detail, name='transistor_detail'),
#     path('prim/<int:transistor_id>/', transistor_primech_change, name='transistor_primech_change'),
#     path('count/<int:transistor_id>/', transistor_count, name='transistor_count'),
#     path('conf/<int:pk>/', transistor_removal_confirmation, name='transistor_removal_confirmation'),
#     path('delete/<int:pk>/', transistor_delete, name='transistor_delete'),
]