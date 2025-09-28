from django.urls import path
from .views import ClientListCreateView  # adjust this to your DRF view

urlpatterns = [
    path('', ClientListCreateView.as_view(), name='client-list'),
]