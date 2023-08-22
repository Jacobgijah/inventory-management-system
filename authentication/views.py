from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from .models import Profile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_authenticated and user.is_staff and user.is_superuser: 
                login(request, user)
                return redirect('index')
            login(request, user)
            return redirect('staff-index')
        messages.error(request, 'Invalid credentials! Try again')
        return render(request, 'authentication/login.html')
    return render(request, 'authentication/login.html')

@login_required
def logout_view(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'authentication/profile.html')

def profile_update(request):
    profile = Profile.objects.get(pk=id)
    context = {
        'profile': profile,
        'values': profile
    }
    if request.method == 'POST':
        
        
        return render(request, 'authentication/profile.html', context)