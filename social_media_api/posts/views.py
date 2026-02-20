from rest_framework import viewsets, generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from notifications.models import Notification  # Your notification app

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


# -----------------------------
# Like Post
# -----------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            content_type=ContentType.objects.get_for_model(post),
            object_id=post.id
        )
        return Response({'message': 'Post liked'}, status=status.HTTP_201_CREATED)

    return Response({'message': 'You already liked this post'}, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# Unlike Post
# -----------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)

    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response({'message': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)
