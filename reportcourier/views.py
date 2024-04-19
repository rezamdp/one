# ===============================================> Imports <===============================================
# ----> general  <----
from django.shortcuts import (render, redirect, get_object_or_404)

from django.urls import (reverse, reverse_lazy)

from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView ,)

from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import *
# ----> external  <----
from .forms import *
from .models import *
from account.models import *


# ===============================================> ReasonBack View <===============================================
class CreateReasonBackView(LoginRequiredMixin, CreateView, ListView):
    model = ReasonBack
    form_class = ReasonBackForm
    template_name = 'reportcourier/add_reasonback.html'


# ----> Class Edit ReasonBack <----
class UpdateReasonBackView(LoginRequiredMixin, UpdateView):
    model = ReasonBack
    form_class = ReasonBackForm
    template_name = 'reportcourier/add_reasonback.html'


# ----> Class Delete ReasonBack <----
class DeleteReasonBackView(LoginRequiredMixin, DeleteView):
    model = ReasonBack
    template_name_suffix = 'reportcourier/add_reasonback.html'
    success_url = reverse_lazy('reportcourier:add_reasonback')


# ================================================> Courier View <================================================
# ----> Class Create Courier <----
class CreateCourierView(LoginRequiredMixin,CreateView, ListView):
    model = Courier
    form_class = CourierForm
    template_name = 'reportcourier/add_courier.html'
    context_object_name = 'object_list'


# ----> Class Edit Courier <----
class UpdateCourierView(LoginRequiredMixin, UpdateView):
    model = Courier
    form_class = CourierForm
    template_name = 'reportcourier/add_courier.html'


# ----> Class Delete Courier <----
class DeleteCourierView(LoginRequiredMixin, DeleteView):
    model = Courier
    success_url = reverse_lazy('reportcourier:add_courier')





# ==============================================> ReportCourier View <==============================================
# ----> Class Create ReportCourier <----
class CreateReportCourierView(LoginRequiredMixin,CreateReportCourierMixin,CreateView):
    model = ReportCuorier
    template_name = 'reportcourier/add_reportcourier.html'
    success_url = reverse_lazy('reportcourier:dashboard_home')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ReportCuorier.objects.all()
        else:
            return ReportCuorier.objects.filter(user=self.request.user)

    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            instance = form.save(commit=False)
            instance.user = self.request.user
            instance.save()
        return super().form_valid(form)

# ----> Class List ReportCourier <----
class ListReportCourierView(LoginRequiredMixin, ListView):
    model = ReportCuorier
    template_name = 'reportcourier/dashboard_home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ReportCuorier.objects.all()
        else:
            return ReportCuorier.objects.filter(user=self.request.user)


class UpdateReportCourierView(LoginRequiredMixin, UpdateView):
    model = ReportCuorier
    template_name = 'reportcourier/update_reportcourier.html'
    form_class = ReportCourierForm
    form_name = 'form'
    success_url = reverse_lazy ('reportcourier:dashboard_home')

class DetailReportCourierView(LoginRequiredMixin, DetailView):
    model = ReportCuorier
    template_name = 'reportcourier/detial_reportcourier.html'
    context_object_name = 'report'


class DeleteReportCourierView(LoginRequiredMixin,DeleteView) :
    model = ReportCuorier
    success_url = reverse_lazy('reportcourier:dashboard_home')
