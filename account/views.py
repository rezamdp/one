#===============================================> Imports <===============================================
# ----> general  <----
from django.shortcuts import render , redirect
from django.views.generic import (
    ListView, CreateView , UpdateView , DeleteView , DetailView ,TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse , reverse_lazy

# ----> external  <----
from .forms import *
from .models import *




class CreateUserView(LoginRequiredMixin,CreateView):
    model = User
    form_class = CreateUserForm
    form_name ='form'
    template_name = 'registration/registeruser.html'
    success_url = reverse_lazy('reportcourier:dashboard_home')




class UpdateUserView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = EditUserForm
    form_name ='form'
    template_name = 'registration/update_user.html'


class ViewUserView(LoginRequiredMixin,ListView):
    model = User
    template_name = 'registration/list_user.html'



