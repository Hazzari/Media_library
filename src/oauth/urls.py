from django.urls import path

from .endpoint import auth_views, views

urlpatterns = [
    path('me/',
         views.UserViewSet.as_view({'get': 'retrieve', 'put': 'update'})),

    path('author/', views.AuthorView.as_view({'get': 'list', })),
    path('author/<int:pk>/', views.AuthorView.as_view({'get': 'retrieve', })),

    path('social/', views.SocialLinkView.as_view(
        {'get': 'list', 'post': 'create', }
    )),
    path('social/<int:pk>', views.SocialLinkView.as_view(
        {'put': 'update', 'delete': 'destroy'}
    )),

    path('spotify-login/', auth_views.spotify_login, name='spotify'),
    path('spotify-callback/', auth_views.spotify_auth),

    path('google-login/', auth_views.google_auth),
    path('google/', auth_views.google_login, name='google'),

    path('', views.link_page, name='index'),

]
