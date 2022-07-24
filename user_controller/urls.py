from django.urls import path, re_path, include

from .views import *



urlpatterns = [
    path( 'auth/', include( 'djoser.urls' ) ),
    re_path( r'^auth/', include( 'djoser.urls.authtoken' ) ),

    path( 'users/',  CustomUserListAPIView.as_view(), name = 'custom_user-list'),
    path( 'users/<int:pk>/',  CustomUserRetrieveAPIView.as_view(), name = 'custom_user-retrieve'),
]