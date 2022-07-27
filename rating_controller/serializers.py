from rest_framework import serializers

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