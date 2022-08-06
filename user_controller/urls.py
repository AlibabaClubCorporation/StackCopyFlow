from django.urls import path, re_path, include

from .views import *



urlpatterns = [
    path( 'auth/', include( 'djoser.urls' ) ),
    re_path( r'^auth/', include( 'djoser.urls.authtoken' ) ),

    path( 'users/',  CustomUserListAPIView.as_view(), name = 'custom_user-list'),
    path( 'users/<int:pk>/',  CustomUserRetrieveAPIView.as_view(), name = 'custom_user-retrieve'),
    path( 'users/<int:pk>/update-rating/', CustomUserRatingUpdateAPIView.as_view(), name = 'custom_user-rating-update' ),

    path( 'appeals/', AppealToUserListAPIView.as_view(), name = 'appeal-list' ),
    path( 'appeals/create/', AppealToUserCreateAPIView.as_view(), name = 'appeal-create' ),

    path( 'bann/', BannAPIView.as_view(), name = 'custom_user-ban' ),
    path( 'unbann/', UnbannAPIView.as_view(), name = 'custom_user-unban' ),
    path( 'banned_users/', BannedUserListAPIView.as_view(), name = 'banned_custom_user-list' ),
]