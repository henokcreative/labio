from django.shortcuts import render, get_object_or_404, redirect
from .models import Message

def dashboard_home(request):
    messages = Message.objects.order_by("-created_at")
    return render(request, "dashboard/list.html", {"messages": messages})

def message_detail(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    return render(request, "dashboard/detail.html", {"message": msg})

def message_reply(request, pk):
    msg = get_object_or_404(Message, pk=pk)

    if request.method == "POST":
        reply_text = request.POST.get("reply")
        msg.reply = reply_text
        msg.handled = True
        msg.save()
        return redirect("message_detail", pk=pk)

    return render(request, "dashboard/reply.html", {"message": msg})