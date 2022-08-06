from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from user_opinion_controller.models import AppealToUser
from forum.permissions import IsSuperUser

from .models import *
from .serializers import *

from user_opinion_controller.serializers import SetRatingSerializer, DisplayAppealToUserSerializer, AppealToUserCreateSerializer




# CUSTOM USER VIEWS

class CustomUserListAPIView( ListAPIView ):
    """
        View class for displaying a list of custom user
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListSerializer

class CustomUserRetrieveAPIView( RetrieveAPIView ):
    """
        View class for displaying a detail information of custom user
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRetrieveSerializer


# RATING VIEW

class CustomUserRatingUpdateAPIView( UpdateAPIView ):
    """
        View class for create/update/delete rating for User from User
    """

    queryset = CustomUser.objects.all()
    serializer_class = SetRatingSerializer
    permission_classes = ( IsAuthenticated, )

# APPEAL VIEW

class AppealToUserListAPIView( ListAPIView ):
    """
        View class for display list appeal to user
    """

    queryset = AppealToUser.objects.all()
    serializer_class = DisplayAppealToUserSerializer
    permission_classes = ( IsSuperUser, )

class AppealToUserCreateAPIView( CreateAPIView ):
    """
        View class for create appeal to user
    """

    serializer_class = AppealToUserCreateSerializer
    
