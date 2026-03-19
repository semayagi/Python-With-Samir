from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# The login_required decorator to protect views
from django.contrib.auth.decorators import login_required

# For class-based views [CBV]
from django.contrib.auth.mixins import LoginRequiredMixin
# For class-based views [CBV]
from django.views import View

from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    error_message = None 
    next_url = request.GET.get('next', '')
    if request.method == "POST":
        form = LoginForm(request.POST)
        next_url = request.POST.get('next') or 'home'
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:   # if the authentication was succesful
                login(request, user)
                return redirect(next_url)
        else:
            error_message = "Invalid Credentials!"
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form, 'error': error_message, 'next': next_url})
            
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')

# Home view
# Using the decorator
@login_required
def home_view(request):
    return render(request, 'auth1_app/home.html') 

# Protected View - anyone who's not loginned is redirected here
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'   # we'll redirect unauthenticated users to this login URL
    # 'next' - to redirect URL
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'registration/protected.html')
    
