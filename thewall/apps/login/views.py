from django.shortcuts import render, redirect
import bcrypt
from .models import *
from django.contrib import messages

# Create your views here.

########################
# INDEX - DISPLAY REGISTRATION FORM AND LOGIN FORM
########################
def registration_login_forms(request):
    if "userid" in request.session:
        return redirect("/wall")
    return render(request, "login/index.html")

######################
# AJAX EMAIL VALIDATION
#######################
def check_email(request):
    found = False
    result = User.objects.filter(email=request.POST["email"])
    if len(result) > 0:
        found = True
    context = {
        "found_html": found
    }
    return render(request, "login/partials/email.html", context)

########################
# AJAX USERNAME VALIDATION
########################
def check_username(request):
    found = False
    result = User.objects.filter(username=request.POST["username"])
    if len(result) > 0:
        found = True
    context = {
        "found_html": found
    }
    return render(request, "login/partials/username.html", context) 

########################
# PROCESS NEW USER ADDITION
########################
def register(request):
    
    if is_original(email, request.POST["email"]) and is_original(username, request.POST["username"]):
        pass
    else:
        messages.error(request, "User already exists.", extra_tags="registration")
        return redirect("/")
    
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="registration")
        return redirect("/")
    new_user = User.objects.add_user(request.POST)
    request.session["userid"] = new_user.id
    messages.success(request, "Successfully registered!")
    return redirect("/wall")

#########################
# LOGIN
##########################
def login(request):
    if User.objects.login(request.POST):
        request.session["userid"] = User.objects.get_id(request.POST)
        messages.success(request, "Successfully logged in!")
        return redirect("/wall")
    else:
        messages.error(request, "You could not be logged in.", extra_tags="login")
        return redirect("/")

##########################
# LOGOUT
###########################
def logout(request):
    request.session.clear()
    return redirect("/")

##########################
# USER HOME - DISPLAY BASIC PROFILE INFO
##########################
def user_home(request, userid):
    if not "userid" in request.session: 
        messages.error(request, "You are not logged in.", extra_tags="login")
        return redirect("/")
    elif int(userid) != int(request.session["userid"]):
        messages.error(request, "You can only view your own dashboard.")
        return redirect(f"/user/{request.session['userid']}/home")
    
    user = User.objects.get(id=request.session["userid"])
    context = {
        "user_html": user
    }
    return render(request, "login/home.html", context)