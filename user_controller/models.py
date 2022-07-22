from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser( AbstractUser ):
    """
        User model class
    """

    REQUIRED_FIELDS = [ 'first_name', 'last_name', 'gender', 'birth_date', 'password', ]

    GENDERS = (
        ( 'm', 'male' ),
        ( 'f', 'female'),
    )

    gender = models.CharField( max_length = 1, choices = GENDERS, default = 'm' )
    birth_date = models.DateField( default = '2002-10-05' )

    class Meta:
        verbose_name = 'Custom users'
        verbose_name_plural = 'Custom user'
        # ordering = [ 'rating', '-birth_date' ]