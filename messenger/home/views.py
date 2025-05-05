from django.views import View
from django.shortcuts import render

class HomeView(View):
    templates_name = 'home.html'