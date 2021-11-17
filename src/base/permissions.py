from rest_framework import permissions


class IsAuthor(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # Метод срабатывает когда при запросах get_object
        # объект это запись из DB
        # проверяем тот же это пользователь что создал запись
        return obj.user == request.user
