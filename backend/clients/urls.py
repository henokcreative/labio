from django.urls import path
from .views import ClientListCreateView, ContractListCreateView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('contracts/', ContractListCreateView.as_view(), name='contract-list-create'),
]