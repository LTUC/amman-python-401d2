from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Snack

# Create your views here.
class HomeView(ListView):
    template_name = 'home.html'
    model = Snack

class SnackDetailsView(DetailView):
    template_name = 'snack_details.html'
    model = Snack
