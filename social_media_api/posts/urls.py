from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

# DRF router for standard CRUD endpoints
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),  # GET /api/feed/
    path('', include(router.urls)),                  # /api/posts/ and /api/comments/
]
