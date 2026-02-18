# blog/urls.py
from django.urls import path
from . import views_auth
from . import views_posts
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Home
    path('', views_auth.home, name='home'),

    # Authentication URLs
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views_auth.register, name='register'),
    path('profile/', views_auth.profile, name='profile'),

    # Blog Post CRUD URLs
    path('posts/', views_posts.PostListView.as_view(), name='post-list'),
    path('posts/new/', views_posts.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views_posts.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views_posts.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views_posts.PostDeleteView.as_view(), name='post-delete'),
]
