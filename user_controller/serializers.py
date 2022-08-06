from rest_framework import serializers

from .models import *

from forum.serilizers import QuestionListSerializer
from user_opinion_controller.services.service_of_rating import RatingManager



# CUSTOM USER SERIALIZERS

class CustomUserRetrieveSerializer( serializers.ModelSerializer ):
    """
        Custom user retrieve serializer
    """

    questions = QuestionListSerializer( many = True )

    is_me = serializers.SerializerMethodField()
    is_rated_by_current_user = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'rating',
            'gender',
            'birth_date',
            'registration_date',
            'questions',

            'is_rated_by_current_user',
            'is_me',
            'id',
        )
    
    def get_is_rated_by_current_user( self, obj ):
        user = self.context['request'].user

        return RatingManager.is_object_having_rating_from_user( user, obj )
    
    def get_is_me( self, obj ):
        if obj == self.context['request'].user:
            return True 
        
        return False

class CustomUserListSerializer( serializers.ModelSerializer ):
    """
        Custom user list serializer
    """

    is_me = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'rating',

            'is_me',
            'id',
        )
    
    def get_is_me( self, obj ):
        if obj == self.context['request'].user:
            return True 
        
        return False