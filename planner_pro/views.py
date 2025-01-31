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
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect("dashboard")  # Redirect to dashboard
    else:
        form = UserCreationForm()
    
    return render(request, "registration/signup.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")  # Redirect after login
    else:
        form = AuthenticationForm()
    
    return render(request, "registration/login.html", {"form": form})
    
# CREATE EVENT - Protected, Only Logged-in Users
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to event list after creation
    else:
        form = EventForm()

    return render(request, 'create_event.html', {'form': form})

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