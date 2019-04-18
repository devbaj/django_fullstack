from django.shortcuts import render, redirect

# Create your views here.

def wall(request):
    return render(request, "wallapp/wall.html")

def send_message(request):
    return redirect("/wall")

def send_comment(request):
    return redirect("/wall")