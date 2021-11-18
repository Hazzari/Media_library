from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file) -> str:
    """Построение пути к файлу аватара,
       format: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/user_{instance.id}/{file}'


def validate_size_img(file_obj):
    """Проверка размера файла
    """
    mb_limit = 2
    if file_obj.size > mb_limit * 1024 * 1024:  # Больше чем 2 мб
        raise ValidationError(f'Максимальный размер файла {mb_limit}MB')


def get_path_upload_cover_album(instance, file) -> str:
    """Построение пути к файлу обложки альбома,
       format: (media)/album/user_id/image.jpg
    """
    print(instance)
    return f'album/user_{instance.id}/{file}'


def get_path_upload_cover_playlist(instance, file) -> str:
    """Построение пути к файлу обложки альбома,
       format: (media)/playlist/user_id/cover.jpg
    """
    return f'playlist/user_{instance.id}/{file}'


def get_path_upload_track(instance, file) -> str:
    """Построение пути к файлу обложки альбома,
       format: (media)/track/user_id/track.[mp3|wav]
    """
    return f'track/user_{instance.id}/{file}'


def get_path_upload_file(instance, file):
    f"""Построение пути к файлу
    format: (media)/{instance.__class__.__name__.lower()}/user_id/{file}
    """
    return f'{instance.__class__.__name__.lower()}/user_{instance.id}/{file}'
