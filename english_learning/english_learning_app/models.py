from django.db import models

class Vocabulary(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField()

class Question(models.Model):
    text = models.TextField()
    correct_answer = models.CharField(max_length=100)

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    vocabulary = models.ManyToManyField(Vocabulary)
    questions = models.ManyToManyField(Question)


class Course(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    description = models.TextField()

