from django.urls import path

from .views import *



urlpatterns = [
    
    # PATH OF QUESTION MODEL 

    path( 'questions/', QuestionListAPIView.as_view(), name = 'question-list' ),
    path( 'questions/create/', QuestionCreateAPIView.as_view(), name = 'question-create' ),
    path( 'questions/<int:pk>/', QuestionRetrieveAPIView.as_view(), name = 'question-retrieve' ),
    path( 'questions/<int:pk>/update/', QuestionUpdateAPIView.as_view(), name = 'question-update' ),
    path( 'questions/<int:pk>/update-correct-answer/', CorrectAnswerInQuestionUpdateAPIView.as_view(), name = 'question-correct-answer-update' ),
    path( 'questions/<int:pk>/update-rating/', QuestionRatingUpdateAPIView.as_view(), name = 'question-rating-update' ),
    path( 'questions/<int:pk>/destroy/', QuestionDestroyAPIView.as_view(), name = 'question-destroy' ),

    # PATH OF ANSWER MODEL

    path( 'answers/create-answer/', AnswerCreateAPIView.as_view(), name = 'answer-create' ),
    path( 'answers/<int:pk>/update-answer/', AnswerUpdateAPIView.as_view(), name = 'answer-update' ),
    path( 'answer/<int:pk>/update-answer-rating/', AnswerRatingUpdateAPIView.as_view(), name = 'answer-rating-update' ),
    path( 'answer/<int:pk>/destroy-answer/', AnswerDestroyAPIView.as_view(), name = 'answer-destroy' ),
]