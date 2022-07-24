from django.urls import path

from .views import *



urlpatterns = [
    path( 'questions/', QuestionListAPIView.as_view(), name = 'question-list' ),
    path( 'questions/create/', QuestionCreateAPIView.as_view(), name = 'question-create' ),
    path( 'questions/<int:pk>/', QuestionRetrieveAPIView.as_view(), name = 'question-retrieve' ),

    path( 'questions/<int:pk>/create-answer/', AnswerCreateAPIView.as_view(), name = 'answer-create' ),
]