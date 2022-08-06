from rest_framework import permissions



class StandartPermission( permissions.BasePermission ):
    """
        Standart permission for forum app
    """

    def has_object_permission(self, request, view, obj):
        try:
            return not request.user.is_banned
        except AttributeError:
            return True
    
    def has_permission(self, request, view):
        try:
            return not request.user.is_banned
        except AttributeError:
            return True

class IsAuthenticated( StandartPermission ):
    """
        Standart is authenticated permission
    """

    def has_object_permission(self, request, view, obj):
        return \
            super().has_object_permission(request, view, obj) \
            and permissions.IsAuthenticated.has_object_permission( self, request, view, obj)
        
    def has_permission(self, request, view):
        return \
            super().has_permission(request, view) \
            and permissions.IsAuthenticated.has_permission( self, request, view )

class IsSuperUser( StandartPermission ):
    """
        Permission class | Access is allowed if user is superuser
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser

    def has_permission(self, request, view):
        return request.user.is_superuser

class IsOwner( StandartPermission ):
    """
        Permission class 
         | 
        Access is allowed if the value of the 'creator' attribute of the model matches that of the user performing the action
    """

    def has_object_permission(self, request, view, obj):
        if obj.creator == request.user:
            return True
        
        return False


class IsOwnerOrSuperUser( StandartPermission ):
    """
        Permission class
         | 
        Access is allowed if user is superuser, or value of the 'creator' attribute of the model matches that of the user performing the action
    """

    def has_object_permission(self, request, view, obj):
        is_owner = IsOwner.has_object_permission( self, request, view, obj )
        is_superuser = IsSuperUser.has_object_permission( self, request, view, obj )

        return \
            is_owner or is_superuser \
            and super().has_object_permission( request, view, obj )

class IsAuthenticatedAndNotOwner( StandartPermission ):
    """
        Permission class
         |
        Access is allowed if user is authenticated and value of the 'creator' attribute of the model not matches that of the user performing the action
    """

    def has_object_permission(self, request, view, obj):
        return \
            permissions.IsAuthenticated.has_object_permission( self, request, view, obj ) \
            and not IsOwner.has_object_permission( self, request, view, obj ) \
            and super().has_object_permission( request, view, obj )