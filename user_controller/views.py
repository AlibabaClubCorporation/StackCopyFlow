from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from user_opinion_controller.models import AppealToUser
from forum.permissions import IsSuperUser, IsAuthenticated

from .models import *
from .serializers import *

from user_opinion_controller.serializers import SetRatingSerializer, DisplayAppealToUserSerializer, AppealToUserCreateSerializer
from user_opinion_controller.services.service_of_appeal import UserBannedController



# CUSTOM USER VIEWS

class CustomUserListAPIView( ListAPIView ):
    """
        View class for displaying a list of custom user
    """

    queryset = CustomUser.objects.filter( groups__name__in = [ 'user', 'admin' ] )
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

# APPEAL VIEWS

class AppealToUserListAPIView( ListAPIView ):
    """
        View class for display list appeal to user
    """

    serializer_class = DisplayAppealToUserSerializer
    permission_classes = ( IsAuthenticated, )

    def get_queryset(self):
        if self.request.user.is_superuser:
            return AppealToUser.objects.all()
        
        return AppealToUser.objects.filter( sender = self.request.user )

class AppealToUserCreateAPIView( CreateAPIView ):
    """
        View class for create appeal to user
    """

    serializer_class = AppealToUserCreateSerializer

# BANNED / UNBANNED VIEWS

class BannAPIView( APIView ):
    """
        View for bann users
    """

    permission_classes = ( IsSuperUser, )

    def post( self, request ):
        """ Ban user """

        banned_user_pk = request.POST.get( 'banned_user_pk' )

        if banned_user_pk == None:
            return Response( data = { 'FIELD ERROR' : 'field "banned_user_pk" is required' }, status = 400 )

        banned_user = CustomUser.objects.get( pk = banned_user_pk )
        UserBannedController.user_blocking( banned_user )

        return Response( status = 201 )

class UnbannAPIView( APIView ):
    """
        View for unbann users
    """

    permission_classes = ( IsSuperUser, )

    def post( self, request ):
        """ Unban user """

        unbanned_user_pk = request.POST.get( 'unbanned_user_pk' )

        if unbanned_user_pk == None:
            return Response( data = { 'FIELD ERROR' : ' field "unbanned_user_pk" is required' }, status = 400 )

        unbanned_user = CustomUser.objects.get( pk = unbanned_user_pk )
        UserBannedController.user_unblocking( unbanned_user )

        return Response( status = 201 )
    
class BannedUserListAPIView( ListAPIView ):
    """
        View for displaying banned users
    """

    queryset = UserBannedController.get_blocked_users()
    serializer_class = CustomUserListSerializer
    permission_classes = ( IsSuperUser, )

