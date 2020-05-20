from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response

from .models import *
from .serializers import *


class QuizCreateAPIView(generics.CreateAPIView):
    """
    Создать опрос
    """
    serializer_class = QuizCreateSerializer
    queryset = Quiz.objects.all()
    

class ListQuizAPIView(generics.ListAPIView):
    """
    Получить список опросов
    """
    serializer_class = QuizCreateSerializer
    queryset = Quiz.objects.all()

            
class QuizChangeAPIView(generics.UpdateAPIView):
    """
    Изменить опрос
    """
    serializer_class = QuizUpdateSerializer
    queryset = Quiz.objects.all()
    
    
class AnswerCreateAPIView(generics.CreateAPIView):
    """
    Создать ответ
    """
    serializer_class = AnswerCreateSerializer
    queryset = Answer.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
class AnswerListAPIView(generics.ListAPIView):
    """
    Получить список ответов определенного пользователя
    """
    serializer_class = AnswerSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['pk']
        user = get_object_or_404(User, id=user_id)
        queryset = Answer.objects.filter(user=user)
        return queryset
