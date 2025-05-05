from django.views import View
from django.shortcuts import render, redirect
from .models import User

class RegistrationView(View):
    templates_name = 'reg.html'

    def post(self, request):
        name = request.POST.get('name')
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        password = request.POST.get('password')
        User.objects.create(username= username, surname=surname, email=email, password= password)
        return redirect('auth')

class AuthorizationView(View):
    templates_name = 'auth.html'