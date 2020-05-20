from django.contrib import admin

from .models import *


class QuizAdmin(admin.ModelAdmin):
    model = Quiz
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name', )


class QuestionsAdmin(admin.ModelAdmin):
    model = Questions
    list_display = ('name', 'type_question' )
    search_fields = ('name', )
    
    
class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ('user', )


class ChoisesAnswersAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ('answer', )
    search_fields = ('answer', )


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(ChoisesAnswers, ChoisesAnswersAdmin)
