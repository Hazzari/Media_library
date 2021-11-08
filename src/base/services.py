from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file) -> str:
    """Построение пути к файлу, format: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/{instance.id}/{file}'


def validate_size_img(file_obj):
    """Проверка размера файла
    """
    mb_limit = 2
    if file_obj.size > mb_limit * 1024 * 1024:  # Больше чем 2 мб
        raise ValidationError(f'Максимальный размер файла {mb_limit}MB')
