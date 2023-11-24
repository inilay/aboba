from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import UserLoginForm
from django.contrib.auth import logout
import random


class HomePage(View):
    template_name = 'random_digits/index.html'
    
    def get(self, request, *args, **kwargs):
        random_number = random.randint(1000, 9999)
        return render(request, self.template_name, {'random_number': f"{random_number}"})


class AuthorizationPage(View):
    template_name = 'random_digits/aut.html'

    def get(self, request, *args, **kwargs):
        flag = False
        if request.user.is_authenticated:
            random_number = random.randint(1000, 9999)
            flag = True
            logout(request) 
            return render(request, self.template_name, {'random_number': f"{random_number}", 'flag': flag})
        else:
            return redirect('login')

class UserLogin(LoginView):
    template_name = 'random_digits/login.html'
    next_page = 'authorization'
    form_class = UserLoginForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Login"
        return context
