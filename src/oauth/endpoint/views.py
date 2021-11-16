from django.shortcuts import render
from rest_framework import parsers, permissions, viewsets

from .. import serializers


class UserViewSet(viewsets.ModelViewSet):
    """ Просмотр и редактирование данных пользователя
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


def link_page(request):
    """ Страница ссылок проекта"""
    return render(request, 'index.html')
