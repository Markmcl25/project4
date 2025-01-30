from django.shortcuts import render, redirect
from .models import Event
from django.utils.timezone import now
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    upcoming_events = Event.objects.filter(date__gte=now()).order_by('date')[:5]  # Next 5 events
    return render(request, 'home.html', {'upcoming_events': upcoming_events})

def create_event(request):
    return render(request, 'create_event.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})   

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')    

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    
    return render(request, "registration/signup.html", {"form": form})    