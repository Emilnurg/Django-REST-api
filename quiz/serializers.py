from rest_framework import serializers

from .models import *


class QuizCreateSerializer(serializers.ModelSerializer):
    """создание Опроса"""

    class Meta:
        model = Quiz
        fields = ('id',
                  'name',
                  'start_date',
                  'end_date',
                  'description',
                  'questions')


class QuizUpdateSerializer(serializers.ModelSerializer):
    """изменение Опроса"""

    class Meta:
        model = Quiz
        fields = ('name',
                  'end_date',
                  'description',
                  'questions')
   

class ChoisesAnswersSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ChoisesAnswers
        fields = '__all__'


class AnswerCreateSerializer(serializers.ModelSerializer):
    """
    создать Ответ
    """
    
    class Meta:
        model = Answer
        fields = ('text_answer',
                  'one_answer',
                  'multiple_answer',
                  'question')


class AnswerSerializer(serializers.ModelSerializer):
    """
    Список ответов
    """
    one_answer = ChoisesAnswersSerialiser()
    multiple_answer = ChoisesAnswersSerialiser(many=True)
    
    class Meta:
        model = Answer
        fields = ('text_answer',
                  'one_answer',
                  'multiple_answer',
                  'question')
