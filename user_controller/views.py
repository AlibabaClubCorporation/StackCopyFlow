from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from user_opinion_controller.models import ComplaintToUser
from forum.permissions import IsSuperUser, IsAuthenticated

from .models import *
from .serializers import *

from user_opinion_controller.serializers import SetRatingSerializer, DisplayComplaintToUserSerializer, ComplaintToUserCreateSerializer, BannedSerializer, UnbannedSerializer
from user_opinion_controller.services.service_of_complaint import UserBannedController



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

# COMPLAINT VIEWS

class ComplaintToUserListAPIView( ListAPIView ):
    """
        View class for display list Complaint to user
    """

    serializer_class = DisplayComplaintToUserSerializer
    permission_classes = ( IsAuthenticated, )

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ComplaintToUser.objects.all()
        
        return ComplaintToUser.objects.filter( sender = self.request.user )

class ComplaintToUserCreateAPIView( CreateAPIView ):
    """
        View class for create Complaint to user
    """

    serializer_class = ComplaintToUserCreateSerializer

# BANNED / UNBANNED VIEWS

class BannAPIView( APIView ):
    """
        View for bann users
    """

    permission_classes = ( IsSuperUser, )

    def post( self, request ):
        """ Ban user """

        serializer = BannedSerializer( data = request.POST )

        serializer.is_valid()

        banned_user = CustomUser.objects.get( pk = serializer.validated_data['pk_of_complained_user'] )
        UserBannedController.user_blocking( banned_user )

        return Response( status = 201 )
        # На самом деле, я не уверен что тут есть необходимость что-то возвращать, в плане сериализатора, я так понима. речь о
        # return Responce( data = serializer.validated_data, status = 201 ), но фактически будет возращаться указанный ключ, и 
        # я не очень понимаю что должно быть возвращенно, это вью по-идеи для совершения действия, результат который должно быть
        # выполнение, или не выполнение поставленной задача, то есть, http коды 201 или другие.
        # Надеюсь обьяснил что я имею ввиду

class UnbannAPIView( APIView ):
    """
        View for unbann users
    """

    permission_classes = ( IsSuperUser, )

    def post( self, request ):
        """ Unban user """

        serializer = UnbannedSerializer( data = request.POST )

        serializer.is_valid()

        banned_user = CustomUser.objects.get( pk = serializer.validated_data['pk_of_unbanned_user'] )
        UserBannedController.user_unblocking( banned_user )

        return Response( status = 201 )
        # На самом деле, я не уверен что тут есть необходимость что-то возвращать, в плане сериализатора, я так понима. речь о
        # return Responce( data = serializer.validated_data, status = 201 ), но фактически будет возращаться указанный ключ, и 
        # я не очень понимаю что должно быть возвращенно, это вью по-идеи для совершения действия, результат который должно быть
        # выполнение, или не выполнение поставленной задача, то есть, http коды 201 или другие.
        # Надеюсь обьяснил что я имею ввиду
    
class BannedUserListAPIView( ListAPIView ):
    """
        View for displaying banned users
    """

    queryset = UserBannedController.get_blocked_users()
    serializer_class = CustomUserListSerializer
    permission_classes = ( IsSuperUser, )

