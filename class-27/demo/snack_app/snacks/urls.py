from django.urls import path, include
from .views import HomeView, SnackDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', SnackDetailsView.as_view(), name='snack_details'),
]




# 127.0.0.1:8000/snacks/4
