# dashboard/views.py
from django.shortcuts import render, get_object_or_404
from clients.models import Message  # <-- use the real Message model

def inbox(request):
    """Simple inbox listing all contact messages."""
    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'dashboard/inbox.html', {'messages': messages})

def message_detail(request, pk):
    """View a single message."""
    message = get_object_or_404(Message, pk=pk)
    return render(request, 'dashboard/message_detail.html', {'message': message})