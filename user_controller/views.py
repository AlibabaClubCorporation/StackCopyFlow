from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView

from .models import ComplaintToUser
from forum.permissions import IsSuperUser, IsAuthenticated

from .models import *
from .serializers import *

from .services.service_of_complaint import UserBannedController



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
    permission_classes = ( IsAuthenticated, )

# BANNED / UNBANNED VIEWS

class UserBannUpdateAPIView( UpdateAPIView ):
    """
        View class for update 'is_banned' user field
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserBannSerializer
    permission_classes = ( IsSuperUser, )
    
class BannedUserListAPIView( ListAPIView ):
    """
        View for displaying banned users
    """

    queryset = UserBannedController.get_blocked_users()
    serializer_class = CustomUserListSerializer
    permission_classes = ( IsSuperUser, )

