from django.shortcuts import render, redirect
from .models import Event
from django.utils.timezone import now
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    """ Display upcoming events (next 5 by default) """
    upcoming_events = Event.objects.filter(date__gte=now()).order_by('date')[:5]  
    return render(request, 'home.html', {'upcoming_events': upcoming_events})

@login_required
def create_event(request):
    """ Placeholder for event creation (TODO: Add event form logic) """
    return render(request, 'create_event.html')

def event_list(request):
    """ Display all events """
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})   

@login_required
def dashboard(request):
    """ Ensure only logged-in users can access dashboard """
    return render(request, 'dashboard.html')    

def signup(request):
    """ User signup using Django's built-in UserCreationForm """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    
    return render(request, "registration/signup.html", {"form": form})    
