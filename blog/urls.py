from django.urls import path
from . import views
from .views import postListView,postDetailView

urlpatterns = [
    path('', postListView.as_view(),name='blog-home'),
    path('post/<int:pk>/',postDetailView.as_view(),name='post-detail'),
     path('about/', views.about,name='blog-about'),
]
