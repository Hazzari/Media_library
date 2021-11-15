from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = ('country', 'city', 'bio', 'display_name', 'avatar',)


class GoogleAuthSerializer(serializers.Serializer):
    """Сериализация данных от Google
    """

    email = serializers.EmailField()
    token = serializers.CharField()
