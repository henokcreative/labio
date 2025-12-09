# dashboard/views.py
from django.shortcuts import render, get_object_or_404, redirect
from clients.models import Message
from django.utils import timezone

def message_inbox(request):
    messages = Message.objects.order_by("-created_at")
    return render(request, "dashboard/message_inbox.html", {"messages": messages})

def message_detail(request, pk):
    message = get_object_or_404(Message, id=pk)
    return render(request, "dashboard/message_detail.html", {"message": message})

def message_reply(request, pk):
    message = get_object_or_404(Message, id=pk)

    if request.method == "POST":
        reply_text = request.POST.get("reply")
        message.reply = reply_text
        message.replied_at = timezone.now()
        message.save()

        # ✔️ Correct redirect using named URL inside namespace
        return redirect("dashboard:message_detail", pk=pk)

    return render(request, "dashboard/message_reply.html", {"message": message})