from django.shortcuts import render, redirect
from .models import *
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
    return redirect("/wall")

def send_comment(request):
    return redirect("/wall")