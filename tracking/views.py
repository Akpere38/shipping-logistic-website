from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Package, StatusUpdate
from .forms import TrackingForm  # We'll create this next

def home(request):
    return render(request, 'tracking/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'tracking/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'tracking/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def track_package(request):
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            tracking_id = form.cleaned_data['tracking_id']
            try:
                package = Package.objects.get(tracking_id=tracking_id)
                updates = package.updates.all().order_by('-timestamp')
                # print("Updates:", [(u.timestamp, u.status, u.location) for u in updates])  # Debug
                return render(request, 'tracking/track_result.html', {'package': package, 'updates': updates})
            except Package.DoesNotExist:
                return render(request, 'tracking/track_result.html', {'package': None})
    else:
        form = TrackingForm()
    return render(request, 'tracking/track.html', {'form': form})