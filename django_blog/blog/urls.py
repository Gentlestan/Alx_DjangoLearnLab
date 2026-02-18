from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # now all views are in one file

urlpatterns = [
    # -------------------------
    # Home & Authentication
    # -------------------------
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

# -------------------------
# Blog Post CRUD
# -------------------------
path('post/new/', views.PostCreateView.as_view(), name='post-create'),
path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
path('post/', views.PostListView.as_view(), name='post-list'),


    # -------------------------
    # Comment CRUD (class-based)
    # -------------------------
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]
