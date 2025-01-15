from django.urls import path
from .views import transistors_all


urlpatterns = [
    path('', transistors_all, name='transistors_all'),
    # path('<int:sort_id>/', sort_detail, name='sort_id'),
    # path('dop/<int:info_id>/', info_detail, name='info_detail'),
    # path('found/', found, name='found'),
]