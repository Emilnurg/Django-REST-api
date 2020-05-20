from django.urls import path

from .views import *


urlpatterns = [

    path('create_quiz', QuizCreateAPIView.as_view()),
    path('list_quiz', ListQuizAPIView.as_view()),
    path('change_quiz/<int:pk>', QuizChangeAPIView.as_view()),
    
    path('create_answer', AnswerCreateAPIView.as_view()),
    path('list_answer/<int:pk>', AnswerListAPIView.as_view()),
]
