from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

from user_opinion_controller.serializers import SetRatingSerializer




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

class CustomUserRatingUpdateAPIView( UpdateAPIView ):
    """
        View class for create/update/delete rating for User from User
    """

    queryset = CustomUser.objects.all()
    serializer_class = SetRatingSerializer
    permission_classes = ( IsAuthenticated, )