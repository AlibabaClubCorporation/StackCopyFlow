from user_controller.models import CustomUser



class UserBannedController:
    """
        Class for management users is_banned status
    """

    @staticmethod
    def user_blocking( user ):
        """
            Blocking 'user'
        """

        user.is_banned = True
        user.save()

    @staticmethod
    def user_unblocking( user ):
        """
            Unblocking 'user'
        """

        user.is_banned = False
        user.save()

    @staticmethod
    def get_blocked_users():
        """
            Get all blocked users
        """

        return CustomUser.objects.filter( is_banned = True )
    
    @classmethod
    def is_blocked_user( cls, user ):
        """
            If user is banned - Return True, else False
        """

        return user in cls.get_blocked_users()
