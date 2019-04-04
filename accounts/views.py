from .forms import LoginForm, SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as _login, logout as _logout


def login(request):
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        _login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    return render(request, 'accounts/login.html', {'form': form})


def signup(request):
    next = request.GET.get('next')
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        _login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    return render(request, 'accounts/signup.html', {'form': form})


def logout(request):
    _logout(request)
    return redirect('/accounts/login')
