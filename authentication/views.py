from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        messages.error(request, 'Invalid credentials! Try again')
        return render(request, 'authentication/login.html')
    return render(request, 'authentication/login.html')

@login_required(login_url='login')
def logout_view(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')
