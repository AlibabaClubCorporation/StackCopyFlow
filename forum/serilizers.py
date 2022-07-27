from rest_framework import serializers

from .models import *
from rating_controller.services.service_of_rating import RatingManager



# LABELS SERIALIZERS

class LabelListSerializer( serializers.ModelSerializer ):
    """
        Label list serializer
    """

    class Meta:
        model = Label
        fields = (
            'name',
        )


# ANSWER SERIALIZERS

class AnswerSerializer( serializers.ModelSerializer ):
    """
        Answer serilizer
    """

    children = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = (
            'creator',
            'content',
            'rating',
            'date_of_creation',
            'children',

            'id',
        )

    def get_children( self, obj ):
        return AnswerSerializer( obj.get_children(), many = True ).data

class AnswerCreateSerializer( serializers.ModelSerializer ):
    """
        Answer create serializer
    """

    creator = serializers.HiddenField( default = serializers.CurrentUserDefault() )

    class Meta:
        model = Answer
        fields = (
            'content',
            'parent',
            'question',

            'creator',
        )
    
    def validate_parent( self, value ):
        if value.question.pk != int(self.initial_data['question']):
            raise serializers.ValidationError( 'The specified "Answer" in the "Parent" field refers to another question' )
        
        return value


# QUESTION SERIALIZERS

class QuestionListSerializer( serializers.ModelSerializer ):
    """
        Question list serializer
    """

    labels = LabelListSerializer( many = True )
    is_answered = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = (
            'title',
            'rating',
            'date_of_creation',
            'labels',
            'is_answered',

            'id',
        )
    
    def get_is_answered( self, obj ):
        return obj.correct_answer != None

class QuestionRetrieveSerializer( serializers.ModelSerializer ):
    """
        Question retrieve serializer
    """

    answers = serializers.SerializerMethodField()
    is_rated_by_current_user = serializers.SerializerMethodField()

    correct_answer = AnswerSerializer( many = False )
    labels = LabelListSerializer( many = True )

    class Meta:
        model = Question
        fields = (
            'title',
            'content',
            'rating',
            'date_of_creation',
            'labels',
            'creator',
            'correct_answer',
            'answers',

            'is_rated_by_current_user',

            'id',
        )

    def get_answers( self, obj ):
        return AnswerSerializer(
            Answer.objects.filter(
                parent = None,
                question = obj,
                correctly_answered_question = None
            ),
            many = True,
        ).data
    
    def get_is_rated_by_current_user( self, obj ):
        user = self.context['request'].user

        return RatingManager.is_object_having_rating_from_user( user, obj )


class QuestionCreateSerializer( serializers.ModelSerializer ):
    """
        Question create serializer
    """

    creator = serializers.HiddenField( default = serializers.CurrentUserDefault() )

    class Meta:
        model = Question
        fields = (
            'title',
            'content',
            'labels',

            'creator',
        )


# OTHER SERIALIZERS

class ContentUpdateSerializer( serializers.Serializer ):
    """
        Serializer for update content field in models
    """

    content = serializers.CharField()

    def update(self, instance, validated_data):
        instance.content = validated_data['content']
        instance.save()

        return instance

class CorrectAnswerUpdateSerializer( serializers.ModelSerializer ):
    """
        Serilizer for update 'correct answer' field in Question
    """

    class Meta:
        model = Question
        fields = (
            'correct_answer',
        )
    
    def validate_correct_answer( self, value ):
        if value.question != self.instance:
            raise serializers.ValidationError( 'Cannot set "correct_answer" field for "Question" to "Answer" with "answer.question" field not equal to "question"' )

        return value