from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            user_to_follow = CustomUser.objects.get(pk=pk)
            if user_to_follow == request.user:
                return Response(
                    {"detail": "You cannot follow yourself."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            request.user.following.add(user_to_follow)
            return Response(
                {"detail": f"You are now following {user_to_follow.username}."},
                status=status.HTTP_200_OK,
            )
        except CustomUser.DoesNotExist:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )


class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            user_to_unfollow = CustomUser.objects.get(pk=pk)
            if user_to_unfollow == request.user:
                return Response(
                    {"detail": "You cannot unfollow yourself."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            request.user.following.remove(user_to_unfollow)
            return Response(
                {"detail": f"You have unfollowed {user_to_unfollow.username}."},
                status=status.HTTP_200_OK,
            )
        except CustomUser.DoesNotExist:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )
