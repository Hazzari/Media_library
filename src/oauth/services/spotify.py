import base64
from typing import Optional

import requests
from django.conf import settings as _s
from rest_framework.exceptions import AuthenticationFailed

from src.oauth.services import base_auth
from ..models import AuthUser


def get_spotify_jwt(code: str) -> Optional[str]:
    """ Запрос к серверу для получения access token
    """
    url = 'https://accounts.spotify.com/api/token'
    basic_str = f'{_s.SPOTIFY_CLIENT_ID}:{_s.SPOTIFY_CLIENT_SECRET}'.encode(
        'ascii')
    basic = base64.b64encode(basic_str)
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:8000/spotify-callback/'
    }
    headers = {
        'Authorization': f'Basic {basic.decode("ascii")}'
    }

    res = requests.post(url, data, headers=headers)
    if res.status_code != 200:
        return None
    r = res.json()
    return r.get('access_token')


def get_spotify_user(token: str) -> Optional[str]:
    url_get_user = 'https://api.spotify.com/v1/me'
    headers = {'Authorization': f'Bearer {token}'}
    res = requests.get(url_get_user, headers=headers)
    r = res.json()
    return r.get('email')


def get_spotify_email(code: str) -> Optional[str]:
    _token = get_spotify_jwt(code)
    if _token is not None:
        return get_spotify_user(_token)
    else:
        return None


def spotify_auth(code: str) -> Optional[dict]:
    email = get_spotify_email(code)
    if email:
        user, _ = AuthUser.objects.get_or_create(email=email)
        return base_auth.create_token(user.id)
    else:
        raise AuthenticationFailed(code=403, detail='Bad token Spotify')
