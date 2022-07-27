from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from user_controller.models import CustomUser


class Rating(models.Model):
    """
        Model of rating
    """

    user = models.ForeignKey(
        CustomUser,
        related_name='likes',
        on_delete = models.SET_NULL,

        null = True
    )
    content_type = models.ForeignKey(
        to = ContentType,
        on_delete=models.CASCADE
    )
    content_object = GenericForeignKey(
        'content_type',
        'object_pk',
    )

    object_pk = models.PositiveIntegerField()

    rating = models.SmallIntegerField(
        default = 0,
    )