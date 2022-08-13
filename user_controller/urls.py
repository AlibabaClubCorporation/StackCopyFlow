from django.urls import path, re_path, include

from .views import *



urlpatterns = [
    path( 'auth/', include( 'djoser.urls' ) ),
    re_path( r'^auth/', include( 'djoser.urls.authtoken' ) ),

    path( 'users/',  CustomUserListAPIView.as_view(), name = 'custom_user-list'),
    path( 'users/banned/', BannedUserListAPIView.as_view(), name = 'banned_custom_user-list' ),
    path( 'users/<int:pk>/',  CustomUserRetrieveAPIView.as_view(), name = 'custom_user-retrieve'),
    path( 'users/<int:pk>/bann/', UserBannUpdateAPIView.as_view(), name = 'custom_user-is_banned-update' ),
    path( 'users/<int:pk>/update-rating/', CustomUserRatingUpdateAPIView.as_view(), name = 'custom_user-rating-update' ),

    path( 'complaints/', ComplaintToUserListAPIView.as_view(), name = 'complaint-list' ),
    path( 'complaints/create/', ComplaintToUserCreateAPIView.as_view(), name = 'complaint-create' ),
]