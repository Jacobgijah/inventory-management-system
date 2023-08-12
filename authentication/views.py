from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                return redirect('index')

        messages.error(request, 'Something went wrong! Try Again')
        return render(request, 'authentication/login.html')

class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('login')