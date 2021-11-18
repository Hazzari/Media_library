from django.core.validators import FileExtensionValidator
from django.db import models

from src.base.services import (
    get_path_upload_cover_album,
    get_path_upload_cover_playlist,
    get_path_upload_track,
    validate_size_img,
)
from src.oauth.models import AuthUser


class License(models.Model):
    """Модель лицензий треков пользователя
    """

    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE,
                             related_name='licenses')
    text = models.TextField(max_length=5000)


class Genre(models.Model):
    """Модель жанров треков
    """
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'


class Album(models.Model):
    """Модель альбомов для треков
    """
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE,
                             related_name='albums')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    private = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to=get_path_upload_cover_album,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']),
                    validate_size_img]
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'


class Track(models.Model):
    """Модель треков
    """
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE,
                             related_name='tracks')
    title = models.CharField(max_length=100)
    license = models.ForeignKey(License,
                                on_delete=models.PROTECT,
                                related_name='license_tracks')
    genre = models.ManyToManyField(Genre, related_name='track_genres')
    album = models.ForeignKey(Album,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True, )
    link_of_author = models.CharField(max_length=500, blank=True, null=True)
    file = models.FileField(
        upload_to=get_path_upload_track,
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    create_at = models.DateTimeField(auto_now_add=True)

    plays_counts = models.PositiveIntegerField(default=0)
    download = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    user_of_likes = models.ManyToManyField(AuthUser,
                                           related_name='likes_tracks')

    def __str__(self):
        return f'{self.user}-{self.title}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.user}-{self.title})'


class Comment(models.Model):
    """Модель комментариев к треку
    """
    user = models.ForeignKey(AuthUser,
                             on_delete=models.CASCADE,
                             related_name='comments')
    track = models.ForeignKey(Track, on_delete=models.CASCADE,
                              related_name='track_comments')

    text = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)


class PlayList(models.Model):
    """Модель плейлистов пользователя
    """
    user = models.ForeignKey(AuthUser,
                             on_delete=models.CASCADE,
                             related_name='play_lists')
    title = models.CharField(max_length=50)
    track = models.ManyToManyField(Track, related_name='track_play_list')
    cover = models.ImageField(
        upload_to=get_path_upload_cover_playlist,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']),
                    validate_size_img]
    )
