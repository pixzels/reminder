from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate


def signup(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('/')

    return render(request, 'accounts/signup.html', {'form': form})
