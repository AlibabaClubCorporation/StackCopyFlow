from rest_framework import serializers

from .models import *



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
    correct_answer = AnswerSerializer( many = False )
    labels = LabelListSerializer( many = True )

    class Meta:
        model = Question
        fields = (
            'title',
            'content',
            'date_of_creation',
            'labels',
            'creator',
            'correct_answer',
            'answers',

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