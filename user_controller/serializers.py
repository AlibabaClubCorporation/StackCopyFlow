from rest_framework import serializers

from .models import *

from forum.serilizers import QuestionListSerializer
from .services.service_of_rating import RatingManager



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

# RATING SERIALIZERS

class SetRatingSerializer( serializers.Serializer ):
    """
        Serializer for set value rating
    """

    rating = serializers.IntegerField()

    def update(self, instance, validated_data):
        user = self.context['request'].user
        rating = validated_data['rating']

        if rating > 0:
            RatingManager.set_positive_rating( user, instance )
        elif rating < 0:
            RatingManager.set_negative_rating( user, instance )
        else:
            RatingManager.destroy_rating( user, instance )

        instance.rating = RatingManager.get_rating_of_object( instance )
        instance.save()
        
        return instance

# COMPLAINT SERIALIZER

class DisplayComplaintToUserSerializer( serializers.ModelSerializer ):
    """
        Serializer for display 'Complaint to user'
    """

    class Meta:
        model = ComplaintToUser
        fields = '__all__'

class ComplaintToUserCreateSerializer( serializers.ModelSerializer ):
    """
        Serializer for create 'Complaint to user'
    """

    sender = serializers.HiddenField( default = serializers.CurrentUserDefault() )

    class Meta:
        model = ComplaintToUser
        fields = '__all__'

# # -- Banned \ Unbanned serializer --

class UserBannSerializer( serializers.ModelSerializer ):
    """
        Serializer for banned/unbanned users
    """

    class Meta:
        model = CustomUser
        fields = ( 'is_banned', )