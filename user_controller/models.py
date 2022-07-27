from django.db import models
from django.contrib.auth.models import AbstractUser


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


    def __str__(self) -> str:
        return f'User: {self.username} | {self.pk}'


    class Meta:
        pass
        ordering = [ '-rating', '-registration_date' ]