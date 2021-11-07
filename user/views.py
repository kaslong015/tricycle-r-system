from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def loginPage(request):
    forms = LoginForm()
    context = {}

    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {'form': forms}
    return render(request, 'login.html', context)


def registerPage(request):
    forms = createUserForm()
    if request.method == 'POST':
        forms = createUserForm(request.POST)
        if forms.is_valid():
            forms.save()
            user = forms.cleaned_data.get('username')

            messages.success(
                request, 'Account was created for' + user + ', log in')
            return redirect('home')

    context = {'forms': forms}
    return render(request, 'register.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/')


def index(request):
    context = {}

    return render(request, 'index.html', context)
