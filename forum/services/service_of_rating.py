from django.contrib.contenttypes.models import ContentType

from forum.models import Rating

from user_controller.models import CustomUser



class RatingManager:
    """
        Class for management rating model
    """

    def set_positive_rating( user, object ):
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
    
    def set_negative_rating( user, object ):
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

    def is_object_having_rating_from_user( user, object ) -> bool:
        """
            Return True, if 'object' have a rating from 'user', else return False
        """

        object_type = ContentType.objects.get_for_model( object )
        rating = Rating.objects.filter(
            content_type = object_type,
            object_pk = object.pk,
            user = user,
        )

        return rating.exists()

    def is_object_having_positive_rating_from_user( user, object ) -> bool:
        """
            Return True, if 'object' have positive rating from 'user', else return False
        """

        object_type = ContentType.objects.get_for_model( object )
        rating = Rating.objects.filter(
            content_type = object_type,
            object_pk = object.pk,
            user = user,
            rating = 1,
        )

        return rating.exists()
    
    def is_object_having_negative_rating_from_user( user, object ) -> bool:
        """
            Return True, if 'object' have negative rating from 'user', else return False
        """

        object_type = ContentType.objects.get_for_model( object )
        rating = Rating.objects.filter(
            content_type = object_type,
            object_pk = object.pk,
            user = user,
            rating = -1,
        )

        return rating.exists()

    def get_positive_rating_of_object( object ):
        """
            Return positive rating count
        """

        object_type = ContentType.objects.get_for_model( object )
        return Rating.objects.filter(
            content_type = object_type,
            object_pk = object.pk,
            rating = 1,
        ).count()
    
    def get_negative_rating_of_object( object ):
        """
            Return negative rating count
        """

        object_type = ContentType.objects.get_for_model( object )
        return Rating.objects.filter(
            content_type = object_type,
            object_pk = object.pk,
            rating = -1,
        ).count()
    
    def get_rating_of_object( object ):
        """
            Return rating of object
        """

        return RatingManager.get_positive_rating_of_object( object ) - RatingManager.get_negative_rating_of_object( object )
    
    def destroy_rating( user, object ):
        """
            Destroy rating of 'object' from 'user'
        """

        object_type = ContentType.objects.get_for_model( object )
        Rating.objects.get(
            content_type = object_type,
            object_pk = object.pk,
            user = user,
        ).delete()

    
    def get_users_who_have_rated_object( object ):
        """
            Return all users who have rated object
        """

        object_type = ContentType.objects.get_for_model( object )
        return CustomUser.objects.filter(
            ratings__content_type = object_type,
            ratings__object_pk = object.pk,
        )