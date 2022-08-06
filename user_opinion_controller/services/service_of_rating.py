from django.contrib.contenttypes.models import ContentType

from user_opinion_controller.models import Rating
from user_controller.models import CustomUser



class RatingManager:
    """
        Class for management Rating model
    """

    @classmethod
    def set_positive_rating( cls, user, object ):
        """
            Creates a positive rating for object from user
        """

        object_type = ContentType.objects.get_for_model( object )
        rating, is_created = Rating.objects.get_or_create(
            content_type = object_type,
            object_pk = object.pk,
            user = user,
        )

        rating.rating = 1
        rating.save()

        return rating
    
    @classmethod
    def set_negative_rating( cls, user, object ):
        """
            Creates a negative rating for object from user
        """

        object_type = ContentType.objects.get_for_model( object )
        rating, is_created = Rating.objects.get_or_create(
            content_type = object_type,
            object_pk = object.pk,
            user = user,
        )

        rating.rating = -1
        rating.save()

        return rating

    @classmethod
    def is_object_having_rating_from_user( cls, user, object ) -> bool:
        """
            Return True, if 'object' have a rating from 'user', else return False
        """

        if user.is_authenticated != True:
            return False

        object_type = ContentType.objects.get_for_model( object )
        rating = Rating.objects.filter(
            content_type = object_type,
            object_pk = object.pk,
            user = user,
        )

        return rating.exists()

    @classmethod
    def is_object_having_positive_rating_from_user( cls, user, object ) -> bool:
        """
            Return True, if 'object' have positive rating from 'user', else return False
        """

        if user.is_authenticated != True:
            return False

        object_type = ContentType.objects.get_for_model( object )
        rating = Rating.objects.filter(
            content_type = object_type,
            object_pk = object.pk,
            user = user,
            rating = 1,
        )

        return rating.exists()
    
    @classmethod
    def is_object_having_negative_rating_from_user( cls, user, object ) -> bool:
        """
            Return True, if 'object' have negative rating from 'user', else return False
        """

        if user.is_authenticated != True:
            return False

        object_type = ContentType.objects.get_for_model( object )
        rating = Rating.objects.filter(
            content_type = object_type,
            object_pk = object.pk,
            user = user,
            rating = -1,
        )

        return rating.exists()

    @classmethod
    def get_positive_rating_of_object( cls, object ):
        """
            Return positive rating of object count
        """

        object_type = ContentType.objects.get_for_model( object )
        return Rating.objects.filter(
            content_type = object_type,
            object_pk = object.pk,
            rating = 1,
        ).count()
    
    @classmethod
    def get_negative_rating_of_object( cls, object ):
        """
            Return negative rating of object count
        """

        object_type = ContentType.objects.get_for_model( object )
        return Rating.objects.filter(
            content_type = object_type,
            object_pk = object.pk,
            rating = -1,
        ).count()
    
    @classmethod
    def get_rating_of_object( cls, object ):
        """
            Return rating of object
        """

        return cls.get_positive_rating_of_object( object ) - cls.get_negative_rating_of_object( object )
    
    @classmethod
    def destroy_rating( cls, user, object ):
        """
            Destroy rating of 'object' from 'user'
        """

        object_type = ContentType.objects.get_for_model( object )
        Rating.objects.get(
            content_type = object_type,
            object_pk = object.pk,
            user = user,
        ).delete()

    @classmethod
    def get_users_who_have_rated_object( cls, object ):
        """
            Return all users who have rated object
        """

        object_type = ContentType.objects.get_for_model( object )
        return CustomUser.objects.filter(
            ratings__content_type = object_type,
            ratings__object_pk = object.pk,
        )