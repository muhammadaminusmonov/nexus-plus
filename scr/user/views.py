from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = RegisterForm()
    ctx = {
        'form': form,
    }
    return render(request, 'register.html', ctx)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    form = LoginForm()
    ctx = {'form': form}
    return render(request, 'login.html', ctx)


def logout_view(request):
    logout(request)
    return redirect('home')