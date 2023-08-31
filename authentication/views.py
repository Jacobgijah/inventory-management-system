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
    profile = Profile.objects.get(staff=request.user)  # Assuming each profile is linked to a user
    
    if request.method == 'POST':
        # Update profile data based on form submission
        profile.company = request.POST.get('company')
        profile.job = request.POST.get('job')
        profile.country = request.POST.get('country')
        profile.address = request.POST.get('address')
        profile.phone = request.POST.get('phone')
        profile.about = request.POST.get('about')
        if request.FILES.get('profileImage'):
            profile.image = request.FILES.get('profileImage')
        profile.save()
        
        messages.success(request, f'Profile data for {profile.staff.username} has been updated successfully')
        return redirect('profile') 

    context = {
        'profile': profile,
        'values': profile,
    }
    
    return render(request, 'authentication/profile.html', context)
