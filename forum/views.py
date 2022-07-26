from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import *
from .serilizers import *
from .permissions import *
from user_controller.models import *


# QUESTION VIEWS

class QuestionListAPIView( ListAPIView ):
    """
        View class for displaying a list of questions
    """

    queryset = Question.objects.all().prefetch_related('labels')
    serializer_class = QuestionListSerializer
    permission_classes = ( AllowAny, )

class QuestionRetrieveAPIView( RetrieveAPIView ):
    """
        View class for displaying a detail information of question
    """

    queryset = Question.objects.all()
    serializer_class = QuestionRetrieveSerializer
    permission_classes = ( AllowAny, )

class QuestionCreateAPIView( CreateAPIView ):
    """
        View class for create question
    """

    serializer_class = QuestionCreateSerializer
    permission_classes = ( IsAuthenticated, )

class QuestionUpdateAPIView( UpdateAPIView ):
    """
        View class for update question
    """

    queryset = Question.objects.all()
    serializer_class = ContentUpdateSerializer
    permission_classes = ( IsOwnerOrSuperUser, )

class CorrectAnswerInQuestionUpdateAPIView( UpdateAPIView ):
    """
        View class for update 'correct_answer' field in question
    """

    queryset = Question.objects.all()
    serializer_class = CorrectAnswerUpdateSerializer
    # permission_classes = 

class QuestionDestroyAPIView( DestroyAPIView ):
    """
        View class for destroy question
    """

    queryset = Question.objects.all()
    permission_classes = ( IsOwnerOrSuperUser, )


# ANSWER VIEWS

class AnswerCreateAPIView( CreateAPIView ):
    """
        View class for create answer
    """

    serializer_class = AnswerCreateSerializer
    permission_classes = ( IsAuthenticated, )

class AnswerUpdateAPIView( UpdateAPIView ):
    """
        View class for update answer
    """

    queryset = Answer.objects.all()
    serializer_class = ContentUpdateSerializer
    permission_classes = ( IsOwnerOrSuperUser, )

class AnswerDestroyAPIView( DestroyAPIView ):
    """
        View class for destroy answer
    """

    queryset = Answer.objects.all()
    permission_classes = ( IsOwnerOrSuperUser, )


# RATING VIEWS

class QuestionRatingUpdateAPIView( UpdateAPIView ):
    """
        View class for create/update rating for Question from User
    """

    queryset = Question.objects.all()
    serializer_class = SetRatingSerializer
    permission_classes = ( IsAuthenticatedAndNotOwner, )