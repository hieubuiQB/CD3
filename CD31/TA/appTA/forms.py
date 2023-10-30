# lesson/forms.py
from django import forms
from .models import Lesson, Course
from ckeditor.widgets import CKEditorWidget

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content']

    content = forms.CharField(widget=CKEditorWidget())


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content']
