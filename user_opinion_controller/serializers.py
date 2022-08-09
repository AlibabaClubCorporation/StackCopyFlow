from rest_framework import serializers

from user_opinion_controller.models import ComplaintToUser

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

# -- Banned \ Unbanned serializer --

class BannedSerializer( serializers.Serializer ):
    """
        Serializer for banned complained user
    """

    pk_of_complained_user = serializers.IntegerField()

class UnbannedSerializer( serializers.Serializer ):
    """
        Serializer for unbanned user
    """

    pk_of_unbanned_user = serializers.IntegerField()