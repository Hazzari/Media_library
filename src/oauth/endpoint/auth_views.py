import urllib.parse

from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .. import serializers
from ..services import google, spotify, spotify_state


def google_login(request):
    """ Страница входа через Google"""
    context = {'google_key_id': settings.GOOGLE_CLIENT_ID}

    return render(request, 'oauth/google_login.html', context=context)


@api_view(["POST"])
def google_auth(request):
    """ Подтверждение авторизации через google
    """
    google_data = serializers.GoogleAuthSerializer(data=request.data)
    if google_data.is_valid():
        token = google.check_google_auth(google_data.data)
        return Response(token)
    else:
        return AuthenticationFailed(code=403, detail='Bad data Google')


def spotify_login(request):
    """ Страница входа через Spotify"""
    uri = (
        urllib.parse.quote("http://localhost:8000/spotify-callback/", safe=''))
    context = {'spotify_state': spotify_state.generate_spotify_state(10),
               'spotify_key_id': settings.SPOTIFY_CLIENT_ID,
               'spotify_redirect_uri': uri,
               'spotify_scope': 'user-read-private user-read-email'
               }
    return render(request, 'oauth/spotify_login.html', context=context)


@api_view(['GET'])
def spotify_auth(request):
    """ Подтверждение авторизации через Spotify."""
    token = spotify.spotify_auth(request.query_params.get('code'))
    return Response(token)
