from rest_framework import permissions



class IsSuperUser( permissions.BasePermission ):
    """
        Permission class | Access is allowed if user is superuser
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser

class IsOwner( permissions.BasePermission ):
    """
        Permission class 
         | 
        Access is allowed if the value of the 'creator' attribute of the model matches that of the user performing the action
    """

    def has_object_permission(self, request, view, obj):
        if obj.creator == request.user:
            return True
        
        return False


class IsOwnerOrSuperUser( permissions.BasePermission ):
    """
        Permission class
         | 
        Access is allowed if user is superuser, or value of the 'creator' attribute of the model matches that of the user performing the action
    """

    def has_object_permission(self, request, view, obj):
        is_owner = IsOwner.has_object_permission( self, request, view, obj )
        is_superuser = IsSuperUser.has_object_permission( self, request, view, obj )

        return is_owner or is_superuser

class IsAuthenticatedAndNotOwner( permissions.BasePermission ):
    """
        Permission class
         |
        Access is allowed if user is authenticated and value of the 'creator' attribute of the model not matches that of the user performing the action
    """

    def has_object_permission(self, request, view, obj):
        return permissions.IsAuthenticated.has_object_permission( self, request, view, obj ) and not IsOwner.has_object_permission( self, request, view, obj )