from django.contrib import admin

from .models import SinhVien, Lesson, UserProfile, Course, GrammarTest, VocabularyTest, VocabularyQuestion, Quiz, Question, Choice
admin.site.register(SinhVien)
# admin.site.register(Vocabulary)
admin.site.register(Lesson)
# admin.site.register(GrammarTopic)
# admin.site.register(GrammarRule)
# admin.site.register(GrammarQuiz)
# admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(VocabularyTest)
admin.site.register(GrammarTest)
admin.site.register(VocabularyQuestion)
# admin.site.register(Test)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)

#
# @admin.register(Choice)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ('text', 'is_correct', 'question')

