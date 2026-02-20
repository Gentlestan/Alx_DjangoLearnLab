from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, like_post, unlike_post

# DRF router for standard CRUD endpoints
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# URL patterns
urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),        # GET /api/feed/
    path('posts/<int:pk>/like/', like_post, name='like'),   # POST /api/posts/<pk>/like/
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike'),  # POST /api/posts/<pk>/unlike/
    path('', include(router.urls)),                        # /api/posts/ and /api/comments/ CRUD
]
