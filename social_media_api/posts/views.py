from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

User = get_user_model()


# -----------------------------
# Post CRUD
# -----------------------------
class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for creating, reading, updating, and deleting posts.
    Users can only edit or delete their own posts.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# -----------------------------
# Comment CRUD
# -----------------------------
class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for creating, reading, updating, and deleting comments.
    Users can only edit or delete their own comments.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# -----------------------------
# Feed Pagination
# -----------------------------
class FeedPagination(PageNumberPagination):
    page_size = 5


# -----------------------------
# Feed View
# -----------------------------
class FeedView(generics.ListAPIView):
    """
    Returns posts from users that the current user follows.
    Ordered by newest first.
    Only accessible to authenticated users.
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = FeedPagination

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
