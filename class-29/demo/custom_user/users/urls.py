from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import SignUpView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),

]
