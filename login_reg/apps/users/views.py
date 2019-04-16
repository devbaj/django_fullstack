from django.shortcuts import render, redirect
import bcrypt
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request, "users/index.html")

#######################
# REGISTER NEW USER
#####################
def process_reg(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        hash1 = bcrypt.hashpw(request.POST["pw"].encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name=request.POST["fname"], last_name=request.POST["lname"],email=request.POST["email"],pw_hash=hash1)
        request.session["userid"] = new_user.id
        messages.success(request, "Successfully registered!")
        return redirect("/success")

#######################
# DISPLAY SUCCESS PAGE
#######################
def success(request):
    if not "userid" in request.session:
        messages.error(request, "You are not logged in.")
        return redirect("/")
    else:
        user = User.objects.get(id=request.session["userid"])
        context = {
            "user_html": user
        }
        return render(request, "users/success.html", context)

#######################
# LOGIN
######################
def login(request):
    # email match?
    try:
        User.objects.get(email=request.POST["email"])
    except:
        messages.error(request,"User does not exist.")
        return redirect("/")
    email_match = User.objects.get(email=request.POST["email"]) 
    print("*"*80)
    print(email_match)
    print("*"*80)
    if bcrypt.checkpw(request.POST["pw"].encode(), email_match.pw_hash.encode()):
        request.session["userid"] = email_match.id
        messages.success(request, "Successfully logged in!")
        return redirect("/success")
    else:
        messages.error(request, "Incorrect password.")
        return redirect("/")

#########################
# LOGOUT
##########################
def logout(request):
    request.session.clear()
    return redirect("/")