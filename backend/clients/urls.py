from rest_framework import routers
from .views import MessageViewSet, ContractViewSet

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'contracts', ContractViewSet, basename='contract')

urlpatterns = router.urls