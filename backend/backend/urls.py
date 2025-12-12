# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clients.views import MessageViewSet, ContractViewSet
from django.http import JsonResponse

router = routers.DefaultRouter()
router.register(r"messages", MessageViewSet, basename="message")
router.register(r"contracts", ContractViewSet, basename="contract")

def home(request):
    return JsonResponse({"message": "Labio Backend is running!"})

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("dashboard/", include("dashboard.urls", namespace="dashboard")),
]