from django.contrib import admin
from .models import Vocabulary, Question, Lesson

admin.site.register(Vocabulary)
admin.site.register(Question)
admin.site.register(Lesson)

