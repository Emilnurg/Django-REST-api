from django.db import models
from django.contrib.auth.models import User


class ChoisesAnswers(models.Model):
    """модель ответов для выбора"""
    answer = models.CharField('Ответ', max_length=255)
    
    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Варианты ответов'
        verbose_name_plural = 'Варианты ответов'
        
        
QUESTIONS_CHOICES = (
    ('TEXT', 'Текстовый ответ'),
    ('ONE', 'Выбор одного ответа'),
    ('MULTIPLE', 'Выбор из множества ответов')
)


class Questions(models.Model):
    """модель вопросов"""
    name = models.CharField('Текст вопроса', max_length=255)
    type_question = models.CharField('Тип вопроса', max_length=8, choices=QUESTIONS_CHOICES)
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    """модель ответов"""
    
    text_answer = models.TextField('Текстовый ответ',
                                   blank=True)
    one_answer = models.ForeignKey(ChoisesAnswers,
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE,
                                   related_name='one_answer',
                                   verbose_name='Ответ с выбором одного варианта')
    multiple_answer = models.ManyToManyField(ChoisesAnswers,
                                    blank=True,
                                    related_name='multiple_answer',
                                    verbose_name='Ответ с выбором нескольких вариантов')
    question = models.ForeignKey(Questions,
                                 on_delete=models.CASCADE,
                                 verbose_name='К какому вопросу относится ответ')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Ответивший пользователь')
                                    
                                    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Quiz(models.Model):
    """модель опроса"""
    name = models.CharField('Название', max_length=255)
    start_date = models.DateField('Дата начала опроса')
    end_date = models.DateField('Дата окончания опроса')
    description = models.TextField('Описание')
    questions = models.ManyToManyField(Questions,
                                       verbose_name='Вопросы')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
