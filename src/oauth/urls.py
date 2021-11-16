from django.urls import path

from .endpoint import auth_views, views

urlpatterns = [
    path('me/',
         views.UserViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('google/', auth_views.google_auth),
    path('spotify-login/', auth_views.spotify_login),
    path('spotify-callback/', auth_views.spotify_auth),
    path('', auth_views.google_login),
]
