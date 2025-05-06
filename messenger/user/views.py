from django.views import View
from django.shortcuts import render, redirect
#from .models import UserModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

class RegistrationView(View):

    def get(self, request):
        return render(request, 'reg.html')

    def post(self, request):
        name = request.POST.get('name')
        username = request.POST.get('username')
        #surname = request.POST.get('surname')
        email = request.POST.get('email')
        #gender = request.POST.get('gender')
        #age = request.POST.get('age')
        password = request.POST.get('password')

        User.objects.create_user(username = username, email=email, password= password)
        return redirect('auth')

class AuthorizationView(View):

    def get(self, request):
        return render(request, 'log.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Проверка на пустые поля
        if not username or not password:
            messages.error(request, 'Введите логин и пароль!')
            return redirect('auth')

        # Пытаемся аутентифицировать пользователя
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему!')
            return redirect('/')  # Редирект на главную страницу или другую
        else:
            messages.error(request, 'Неверный логин или пароль.')
            return redirect('auth')  # Редирект обратно на страницу авторизации