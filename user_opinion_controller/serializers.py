from dataclasses import fields
from rest_framework import serializers

from user_opinion_controller.models import AppealToUser

from .services.service_of_rating import RatingManager


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

# APPEAL SERIALIZER

class DisplayAppealToUserSerializer( serializers.ModelSerializer ):
    """
        Serializer for display 'appeal to user'
    """

    class Meta:
        model = AppealToUser
        fields = '__all__'

class AppealToUserCreateSerializer( serializers.ModelSerializer ):
    """
        Serializer for create 'appeal to user'
    """

    sender = serializers.HiddenField( default = serializers.CurrentUserDefault() )

    class Meta:
        model = AppealToUser
        fields = '__all__'