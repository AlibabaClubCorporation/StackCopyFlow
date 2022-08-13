from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class CustomUser( AbstractUser ):
    """
        User model class
    """

    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'gender',
        'birth_date',
    ]

    GENDERS = (
        ( 'm', 'male' ),
        ( 'f', 'female'),
    )

    gender = models.CharField(
        max_length = 1,
        choices = GENDERS,
        default = 'm'
    )

    birth_date = models.DateField()

    rating = models.IntegerField( default = 0 )

    registration_date = models.DateTimeField(
        auto_now_add = True,
    )

    is_banned = models.BooleanField(
        default = False
    )

    def __str__(self) -> str:
        return f'User: {self.username} | {self.pk}'


    class Meta:
        pass
        ordering = [ '-rating', '-registration_date' ]


# User opinion models

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


class ComplaintToUser( models.Model ):
    """
        Model of Complaint to user
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