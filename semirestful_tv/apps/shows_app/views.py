from django.shortcuts import render, HttpResponse, redirect
from .models import *
from time import strftime, strptime
from django.contrib import messages

# Create your views here.



def index(request):
    return redirect("/shows")

###########################
# DISPLAY ALL SHOWS
###########################
def shows(request):
    
    all_shows = Show.objects.all()
    context = {
        "all_shows_html": all_shows
    }
    
    return render(request, "shows_app/index.html", context)

###########################
# DISPLAY ADD SHOW TEMPLATE
###########################
def new_show(request):
    
    return render(request, "shows_app/addnew.html")

###########################
# ADD SHOW TO DB
###########################
def add_new_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    
    else:
        new_show = Show.objects.create(title=request.POST["title"], network=request.POST["network"], release_date=request.POST["release_date"], desc = request.POST["desc"])
        new_show_id = new_show.id
        messages.success(request, "Show successfully added.")
        return redirect(f"/shows/{new_show_id}")

###########################
# DISPLAY SHOW INFO
###########################
def display_show(request, show_id):
    
    new_show = Show.objects.get(id=show_id)
    format_release = new_show.release_date.strftime('%d %B, %Y')
    context = {
        "release_date_html": format_release,
        "show_html": new_show,
    }
    
    return render(request, "shows_app/viewshow.html", context)


###########################
# EDIT SHOW ENTRY
###########################
def edit_show(request, show_id):
    show = Show.objects.get(id=show_id)
    context= {
        "show_html": show
    }
    messages.success(request, "Show successfully updated.")
    return render(request, "shows_app/editshow.html", context)

###########################
# SUBMIT EDIT
###########################
def process_edit(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{show_id}/edit")
    else:
        show = Show.objects.get(id=show_id)
        show.save()
        return redirect(f"/shows/{show_id}")

###########################
# REMOVE SHOW FROM DB
###########################
def remove_show(request, show_id):
    
    show = Show.objects.get(id=show_id)
    show.delete()
    
    return redirect("/shows")