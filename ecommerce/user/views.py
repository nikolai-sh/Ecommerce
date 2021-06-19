from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')         
            login(request, user)
            messages.success(request, f'Ваш аккаунт зарегестрирован {username}!')
            return redirect('home')
        else:
            messages.info(request, f'Регистрация не удалась! Неверные данные!')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

