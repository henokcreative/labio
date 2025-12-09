from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.http import JsonResponse
from clients.views import MessageViewSet, ContractViewSet

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'contracts', ContractViewSet, basename='contract')

def home(request):
    return JsonResponse({"message": "Labio Backend is running!"})

urlpatterns = [
    path('', home),  # Root endpoint
    path('admin/', admin.site.urls),

    # API
    path('api/', include(router.urls)),

    # Dashboard (IMPORTANT → add namespace)
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    
]