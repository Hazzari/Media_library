from datetime import datetime, timedelta

import jwt
from django.conf import settings


def create_token(user_id: int) -> dict:
    """ Создание токена
    """
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        'user_id': user_id,
        'access_token': create_access_token(
            data={'user_id': user_id},
            expires_data=access_token_expires,
        ),
        'token_type': 'Token'
    }


def create_access_token(*, data: dict, expires_data: timedelta = None):
    """ Создание access токена 15 минут или сутки
    """

    to_encode = data.copy()
    if expires_data is not None:
        expire = datetime.utcnow() + expires_data
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire, 'sub': 'access'})
    encode_jwt = jwt.encode(to_encode,
                            settings.SECRET_KEY,
                            algorithm=settings.ALGORITHM)
    return encode_jwt
