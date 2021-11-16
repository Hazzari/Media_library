from django.urls import path

from .endpoint import auth_views, views

urlpatterns = [
    path('me/',
         views.UserViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('spotify-login/', auth_views.spotify_login, name='spotify'),
    path('spotify-callback/', auth_views.spotify_auth),
    path('google-login/', auth_views.google_auth),
    path('google/', auth_views.google_login, name='google'),
    path('', views.link_page, name='index'),

]
