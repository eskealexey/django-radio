from django.urls import path


from .views import moduls_all, moduls_tip_list, moduls_nazn_list, datasheet_modul_add, modul_add, modul_edit, \
    modul_detail, modul_primech_change, modul_count, \
    modul_removal_confirmation, modul_removal_confirmation, modul_delete


urlpatterns = [
    path('', moduls_all, name='moduls_all'),
    path('<int:pk>/', moduls_tip_list, name='moduls_tip_list'),
    path('naznachenie/<int:nazn_id>/', moduls_nazn_list, name='moduls_nazn_list'),
    path('add/', modul_add, name='modul_add'),
    path('detail/<int:pk>/', modul_detail, name='modul_detail'),
    path('edit/<int:pk>/', modul_edit, name='modul_edit'),
    path('datasheetadd/', datasheet_modul_add, name='datasheet_modul_add'),
    path('prim/<int:pk>/', modul_primech_change, name='modul_primech_change'),
    path('count/<int:pk>/', modul_count, name='modul_count'),
    path('conf/<int:pk>/', modul_removal_confirmation, name='modul_removal_confirmation'),
    path('delete/<int:pk>/', modul_delete, name='modul_delete'),
]