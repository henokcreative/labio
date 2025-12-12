# dashboard/urls.py
from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.message_inbox, name="message_inbox"),
    path("message/<int:pk>/", views.message_detail, name="message_detail"),
    path("message/<int:pk>/reply/", views.message_reply, name="message_reply"),
]