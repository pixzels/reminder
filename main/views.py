from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reminder
from .forms import InputForm
from django.utils import timezone
import datefinder


@login_required
def home(request):
    input_form = InputForm()
    reminders = Reminder.objects.filter(user=request.user).order_by('due_date')
    return render(request, 'main/home.html', {'reminders': reminders, 'input_form': input_form})


@login_required
def delete(request, uuid):
    Reminder.objects.filter(id=uuid).delete()
    return redirect('/')


@login_required
def add(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data.get('body')
            reminder = form.save(commit=False)
            reminder.user = request.user

            l = datefinder.find_dates(body, base_date=timezone.now().replace(
                hour=0, minute=0, second=0, microsecond=0), source=True)

            for date_time, source in l:
                cleaned_body = body.replace(source, '')
                reminder.due_date = date_time
                reminder.body = cleaned_body

            reminder.save()

    return redirect('/')


def extract_date(s, now):
    if 'today' in s:
        return now.replace(now.hour+2)
    elif 'tomorrow' in l:
        return now.replace(day=now.day+1)
    elif 'day after tomorrow' in l:
        return now.replace(day=now.day+2)
