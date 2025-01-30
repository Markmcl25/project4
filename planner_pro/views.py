from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.utils.timezone import now
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# HOME PAGE - Display upcoming events
def home(request):
    upcoming_events = Event.objects.filter(date__gte=now()).order_by('date')[:5]  # Show next 5 events
    return render(request, 'home.html', {'upcoming_events': upcoming_events})

@login_required
def profile(request):
    return render(request, "profile.html", {"user": request.user})
    
# SIGNUP - Create a new account
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login after signup
    else:
        form = UserCreationForm()
    
    return render(request, "registration/signup.html", {"form": form})

# CREATE EVENT - Protected, Only Logged-in Users
@login_required
def create_event(request):
    return render(request, 'create_event.html')

# EVENT LIST - Show all events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})   

# EVENT DETAIL - Show a single event
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})

# DASHBOARD - Protected, Only Logged-in Users
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')