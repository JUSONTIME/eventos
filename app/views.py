from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Registration
from .forms import EventForm

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

@login_required
def register_event(request, event_id):
    event = Event.objects.get(id=event_id)
    Registration.objects.create(event=event, user=request.user)
    return redirect('event_list')
