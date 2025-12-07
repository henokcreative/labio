from django.contrib import admin
from .models import Message as ContactMessage

admin.site.register(ContactMessage)