from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from .models import *
from user_controller.models import *
from .serilizers import *


# QUESTION VIEWS

class QuestionListAPIView( ListAPIView ):
    """
        View class for displaying a list of questions
    """

    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer

class QuestionRetrieveAPIView( RetrieveAPIView ):
    """
        View class for displaying a detail information of question
    """

    queryset = Question.objects.all()
    serializer_class = QuestionRetrieveSerializer

class QuestionCreateAPIView( CreateAPIView ):
    """
        View class for create question
    """

    serializer_class = QuestionCreateSerializer

class QuestionUpdateAPIView( UpdateAPIView ):
    """
        View class for update question
    """

    queryset = Question.objects.all()
    serializer_class = ContentUpdateSerializer

class QuestionDestroyAPIView( DestroyAPIView ):
    """
        View class for destroy question
    """

    queryset = Question.objects.all()


# ANSWER VIEWS

class AnswerCreateAPIView( CreateAPIView ):
    """
        View class for create answer
    """

    serializer_class = AnswerCreateSerializer

class AnswerUpdateAPIView( UpdateAPIView ):
    """
        View class for update answer
    """

    queryset = Answer.objects.all()
    serializer_class = ContentUpdateSerializer

class AnswerDestroyAPIView( DestroyAPIView ):
    """
        View class for destroy answer
    """

    queryset = Answer.objects.all()