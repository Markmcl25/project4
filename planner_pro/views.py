from django.shortcuts import render
from .models import Event
from django.utils.timezone import now

def home(request):
    upcoming_events = Event.objects.filter(date__gte=now()).order_by('date')[:5]  # Next 5 events
    return render(request, 'home.html', {'upcoming_events': upcoming_events})

def create_event(request):
    return render(request, 'create_event.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})    