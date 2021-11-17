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


class SocialLinkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)  # Для id необязательно

    class Meta:
        model = models.SocialLink
        fields = ('id', 'link',)


class AuthorSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True)

    class Meta:
        model = models.AuthUser
        fields = ('id', 'country', 'city', 'bio', 'display_name', 'avatar', 'social_links')
