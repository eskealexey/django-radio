from django.urls import path
from .views import transistors_all, transistors_list_tip


urlpatterns = [
    path('', transistors_all, name='transistors_all'),
    path('<int:tiptrans_id>/', transistors_list_tip, name='transistors_tip_list'),
    # path('dop/<int:info_id>/', info_detail, name='info_detail'),
    # path('found/', found, name='found'),
]