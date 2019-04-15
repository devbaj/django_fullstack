from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.


###########################
# DISPLAY ALL SHOWS
###########################
def index(request):
    
    return render(request, "shows_app/index.html")

###########################
# DISPLAY ADD SHOW TEMPLATE
###########################
def new_show(request):
    
    return render(request, "shows_app/addnew.html")

###########################
# ADD SHOW TO DB
###########################
def add_new_show(request):
    
    new_show = Show.objects.create(title=request.POST["title"], network=request.POST["network"], release_date=request.POST["release_date"], desc = request.POST["desc"])
    new_show_id = new_show.id
    
    return redirect(f"shows/{new_show_id}")

###########################
# DISPLAY SHOW INFO
###########################
def display_show(request, show_id):
    
    return render(request, "viewshow.html", context)


###########################
# EDIT SHOW ENTRY
###########################
def edit_show(request, show_id):
    
    return render(request, "editshow.html", context)

###########################
# SUBMIT EDIT
###########################
def process_edit(request, show_id):
    
    return redirect(f"shows/{show_id}")

###########################
# REMOVE SHOW FROM DB
###########################
def remove_show(request, show_id):
    
    return redirect("/shows")