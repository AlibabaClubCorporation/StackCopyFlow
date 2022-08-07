from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from user_controller.models import CustomUser



class Rating( models.Model ):
    """
        Model of rating
    """

    user = models.ForeignKey(
        CustomUser,
        related_name='ratings',
        on_delete = models.SET_NULL,

        null = True
    )

    content_type = models.ForeignKey(
        to = ContentType,
        on_delete=models.CASCADE,

        related_name = 'received_rating'
    )
    content_object = GenericForeignKey(
        'content_type',
        'object_pk',
    )

    object_pk = models.PositiveIntegerField()

    rating = models.SmallIntegerField(
        default = 0,
    )


class AppealToUser( models.Model ):
    """
        Model of appeal to user
    """

    sender = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,

        related_name='appeal_to_users',
    )

    receiver = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,

        related_name='received_appeals',
    )

    content = models.CharField( 
        max_length = 2500,
    )