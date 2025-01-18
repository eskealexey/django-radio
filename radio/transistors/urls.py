from django.urls import path
from .views import transistors_all, transistors_list_tip, transistors_list_tip_korpus # found_transistors


urlpatterns = [
    path('', transistors_all, name='transistors_all'),
    path('<int:tiptrans_id>/', transistors_list_tip, name='transistors_tip_list'),
    path('<int:tiptrans_id>/<int:korpus_id>', transistors_list_tip_korpus, name='transistors_list_tip_korpus'),
    # path('found/', found_transistors, name='found_transistors'),
]