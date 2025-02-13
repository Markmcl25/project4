from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User  
from django.contrib import messages
from .models import Booking, Event
from .forms import EventForm
from django.utils.timezone import now
from django.contrib.auth import login, logout
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
            event = form.save(commit=False)
            event.creator = request.user  # Assign the logged-in user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    
    return render(request, 'create_event.html', {'form': form})

# Edit Event
@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user != event.creator and not request.user.is_superuser:
        messages.error(request, "You don't have permission to edit this event.")
        return redirect('event_detail', event_id=event.id)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully.")
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)

    return render(request, 'edit_event.html', {'form': form, 'event': event})

# Delete Event
@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user != event.creator and not request.user.is_superuser:
        messages.error(request, "You don't have permission to delete this event.")
        return redirect('event_detail', event_id=event.id)

    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event deleted successfully.")
        return redirect('event_list')

    return render(request, 'confirm_delete.html', {'event': event})

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
    total_events = Event.objects.count()  # Integer ✅
    upcoming_events_list = Event.objects.filter(date__gte=now()).order_by('date')[:5]  # QuerySet ✅
    upcoming_events_count = upcoming_events_list.count()  # Integer ✅
    total_users = User.objects.count()  # Integer ✅
    pending_bookings_list = Booking.objects.filter(status='pending')  # QuerySet ✅
    pending_bookings_count = pending_bookings_list.count()  # Integer ✅

    context = {
        'total_events': total_events,  # Integer ✅
        'upcoming_events': upcoming_events_list,   # QuerySet ✅
        'upcoming_events_count': upcoming_events_count,  # Integer ✅
        'total_users': total_users,  # Integer ✅
        'pending_bookings': pending_bookings_list,  # QuerySet ✅
        'pending_bookings_count': pending_bookings_count,  # Integer ✅
    }
    return render(request, 'dashboard.html', context)

@login_required
def pending_bookings(request):
    bookings = Booking.objects.filter(status='pending')
    return render(request, 'pending_bookings.html', {'bookings': bookings})

def custom_logout(request):
    logout(request)
    return redirect("home")   