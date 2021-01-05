from django.urls import path, include
from .views import HomeView, SnackDetailsView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', SnackDetailsView.as_view(), name='snack_details'),
    path('add/', SnackCreateView.as_view(), name='snack_create'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name='snack_update'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name='snack_delete'),

]




# 127.0.0.1:8000/snacks/4
