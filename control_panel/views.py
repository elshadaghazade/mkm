from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import views
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

class LoginView(views.LoginView):
    # redirect_field_name = 'redirect_to'
    template_name = "login/login.html"

@login_required(login_url=reverse_lazy('cpanel_login_page'))
def home_view(request):
    return render(request, 'home/home.html')