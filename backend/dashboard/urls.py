# dashboard/urls.py
from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("messages/<int:pk>/", views.message_detail, name="message_detail"),
]