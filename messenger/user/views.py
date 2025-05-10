from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

class RegistrationView(View):

    def get(self, request):
        return render(request, 'reg.html')

    def post(self, request):
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким логином уже существует.')
            return redirect('reg')

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Вы успешно зарегистрированы! Войдите.')
        return redirect('auth')

class AuthorizationView(View):

    def get(self, request):
        return render(request, 'log.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'Введите логин и пароль!')
            return redirect('auth')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему!')
            return redirect('home')
        else:
            messages.error(request, 'Неверный логин или пароль.')
            return redirect('auth')