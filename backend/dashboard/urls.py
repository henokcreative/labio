from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_home, name="dashboard_home"),
    path("message/<int:pk>/", views.message_detail, name="message_detail"),
    path("message/<int:pk>/reply/", views.message_reply, name="message_reply"),
]