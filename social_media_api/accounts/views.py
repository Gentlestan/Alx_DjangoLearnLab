from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer, LoginSerializer

User = get_user_model()


# -----------------------------
# User Registration
# -----------------------------
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    # Token is created inside the serializer


# -----------------------------
# User Login
# -----------------------------
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )


# -----------------------------
# Follow another user
# -----------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)

    if target_user == request.user:
        return Response(
            {"error": "You cannot follow yourself."},
            status=status.HTTP_400_BAD_REQUEST
        )

    if target_user in request.user.following.all():
        return Response(
            {"error": "You already follow this user."},
            status=status.HTTP_400_BAD_REQUEST
        )

    request.user.following.add(target_user)
    return Response(
        {"message": f"You are now following {target_user.username}"},
        status=status.HTTP_200_OK
    )


# -----------------------------
# Unfollow another user
# -----------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)

    if target_user == request.user:
        return Response(
            {"error": "You cannot unfollow yourself."},
            status=status.HTTP_400_BAD_REQUEST
        )

    request.user.following.remove(target_user)
    return Response(
        {"message": f"You have unfollowed {target_user.username}"},
        status=status.HTTP_200_OK
    )
