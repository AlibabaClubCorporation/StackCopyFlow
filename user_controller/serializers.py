from rest_framework import serializers

from forum.serilizers import QuestionListSerializer
from .models import *



# CUSTOM USER SERIALIZERS

class CustomUserRetrieveSerializer( serializers.ModelSerializer ):
    """
        Custom user retrieve serializer
    """

    questions = QuestionListSerializer( many = True )

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'gender',
            'birth_date',
            'registration_date',
            'questions',

            'id',
        )

class CustomUserListSerializer( serializers.ModelSerializer ):
    """
        Custom user list serializer
    """

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',

            'id',
        )