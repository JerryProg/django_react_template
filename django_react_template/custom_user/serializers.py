from rest_framework import serializers
from django.contrib.auth import get_user_model

CUsers = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CUsers
        fields = ['email', 'username', 'last_login']