from django.shortcuts import render, redirect

# Create your views here.

def display_events(request):
    context = {}
    return render(request, "party/eventlist.html", context)

def display_one_event(request, eventid):
    context = {}
    return render(request, "party/eventpage.html", context)

def destroy_event(request):
    # if user owns event
    # pass
    # return to list of events
    # else error
    return redirect(f"/events/{eventid}/")

def dashboard(request):
    context = {}
    return render(request, "party/dashboard.html", context)

def create_event_form(request):

    return render(request, "party/createform.html")

def add_show(request):

    return redirect(f"/party/events/{new_event.id}")