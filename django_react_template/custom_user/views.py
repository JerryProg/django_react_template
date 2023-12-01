from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth import get_user_model
from custom_user.serializers import UserSerializer


# Create your views here.
CUsers = get_user_model()
class UsersList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = CUsers.objects.all()


class CurrentUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return CUsers.objects.filter(email=self.request.user.email)