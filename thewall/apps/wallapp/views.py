from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def wall(request):
    user = User.objects.get(id=request.session["userid"])
    all_messages = Message.objects.all()
    context = {
        "user_html": user,
        "all_messages_html": all_messages
    }
    return render(request, "wallapp/wall.html", context)

def send_message(request):
    sent = Message.objects.add_message(request.session["userid"],request.POST)
    if sent:
        messages.success(request, "Message sent!")
    else:
        messages.error(request, "Unable to send message.")
    return redirect("/wall")

def send_comment(request):
    posted = Comment.objects.add_comment(request.session["userid"], request.POST)
    if posted:
        messages.success(request, "Comment sent!")
    else:
        messages.error(request, "Unable to send comment.")
    return redirect("/wall")