from django.contrib import admin
from django.urls import path, include


from .views import PostDetailsView, PostsListView


urlpatterns = [
    path('', PostsListView.as_view(), name='posts'),
    path('<int:pk>/', PostDetailsView.as_view(), name='post_details'),
]
