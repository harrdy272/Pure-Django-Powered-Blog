from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]