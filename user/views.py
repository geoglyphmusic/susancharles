from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomRegisterForm, CustomChangeForm

# Create your views here.
def register(request):
    form = CustomRegisterForm()

    if request.method == 'POST':
        form = CustomRegisterForm(request.POST) #We have to declare the form again to stop error messages showing up before form is used
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)
            return redirect('login')
    return render(request, 'user/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            messages.success(request, 'You are logged in.')
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'user/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='login')
def account(request):
    return render(request, 'user/account.html')

@login_required(login_url='login')
def edit_profile(request):
    form = CustomChangeForm()

    def get_object(self):
        return self.request.user

    if request.method == 'POST':
        form = CustomChangeForm(request.POST) #We have to declare the form again to stop error messages showing up before form is used
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account changed for ' + user)
            return redirect('account')
    return render(request, 'user/edit_profile.html', {'form': form})
