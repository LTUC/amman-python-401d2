from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Snack

# Create your views here.
class HomeView(ListView):
    template_name = 'home.html'
    model = Snack

class SnackDetailsView(DetailView):
    template_name = 'snack_details.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields = ['name', 'rank', 'eater']

class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = ['name', 'rank', 'eater']

class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    fields = ['name', 'rank', 'eater']
    success_url = reverse_lazy('home')
