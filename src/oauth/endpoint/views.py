from django.shortcuts import render
from rest_framework import parsers, permissions, viewsets

from .. import serializers, models
from ...base.permissions import IsAuthor


def link_page(request):
    """ Страница ссылок проекта.
    """
    return render(request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):
    """ Просмотр и редактирование данных пользователя.
    """
    # Обработка формы и файла одним запросом
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # пользователь который авторизован на сайте.
        # переопределяем что бы получить доступ к self.
        return self.request.user

    def get_object(self):
        # Ссылаемся на самого пользователя
        return self.get_queryset()


class AuthorView(viewsets.ReadOnlyModelViewSet):
    """ Список авторов.
    """
    queryset = models.AuthUser.objects.all().prefetch_related('social_links')
    serializer_class = serializers.AuthorSerializer


class SocialLinkView(viewsets.ModelViewSet):
    """ CRUD ссылок социальных сетей пользователя.
    """
    serializer_class = serializers.SocialLinkSerializer
    permission_classes = [IsAuthor, ]

    def get_queryset(self):
        return self.request.user.social_links.all()

    def perform_create(self, serializer):
        # Связь с юзером
        serializer.save(user=self.request.user)
