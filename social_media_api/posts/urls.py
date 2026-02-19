from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed

# DRF router for standard CRUD endpoints
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# Include feed explicitly as it's a function-based view
urlpatterns = [
    path('feed/', feed, name='feed'),       # GET /api/posts/feed/
    path('', include(router.urls)),          # /api/posts/ and /api/comments/ CRUD
]
