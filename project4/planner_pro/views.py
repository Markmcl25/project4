from django.shortcuts import render
from .models import Event
from django.utils.timezone import now

def home(request):
    upcoming_events = Event.objects.filter(date__gte=now()).order_by('date')[:5]  # Next 5 events
    return render(request, 'home.html', {'upcoming_events': upcoming_events})
