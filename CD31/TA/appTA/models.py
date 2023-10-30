from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor.fields import RichTextField

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class SinhVien (models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=100)
    grade = models.IntegerField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
# class Vocabulary(models.Model):
#     word = models.CharField(max_length=100)
#     definition = models.TextField()
#     example_sentence = models.TextField()
class Course(models.Model):
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100, default="Unknown Instructor")
    description = models.TextField()  # Thay vì models.TextField()
    image = models.ImageField(upload_to='course_images/', default='default.jpg')

    def __str__(self):
        return self.title
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    order = models.PositiveIntegerField(default=0)  # Thêm trường order để xác định thứ tự

    # Các trường khác và phương thức

    def previous_lesson(self):
        return Lesson.objects.filter(course=self.course, order__lt=self.order).last()

    def next_lesson(self):
        return Lesson.objects.filter(course=self.course, order__gt=self.order).first()

    def __str__(self):
        return self.title

# class Test(models.Model):
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     content = models.TextField(default='')
#     order = models.PositiveIntegerField(default=0)  # Thêm trường order để xác định thứ tự
#
#     # Các trường khác và phương thức
#
#     def previous_lesson(self):
#         return Test.objects.filter(course=self.lesson, order__lt=self.order).last()
#
#     def next_lesson(self):
#         return Test.objects.filter(course=self.lesson, order__gt=self.order).first()
#
#     def __str__(self):
#         return self.title


class GrammarTopic(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()

class GrammarRule(models.Model):
    topic = models.ForeignKey(GrammarTopic, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    explanation = models.TextField()
    examples = models.TextField()

class GrammarQuiz(models.Model):
    rule = models.ForeignKey(GrammarRule, on_delete=models.CASCADE)
    question = models.TextField()
    correct_answer = models.CharField(max_length=100)
    wrong_answers = models.TextField()




class UserProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=100, unique=True)
    # password = models.CharField(max_length=100)
    # email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=100, unique=True)
    adress = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
class SessionToken(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)

class VocabularyTest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time_limit_minutes = models.IntegerField()
    number_of_questions = models.IntegerField()


    def __str__(self):
        return self.title
class VocabularyQuestion(models.Model):
    test = models.ForeignKey(VocabularyTest, on_delete=models.CASCADE)
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=100)
    wrong_answer1 = models.CharField(max_length=100, default="Default Wrong Answer 1")
    wrong_answer2 = models.CharField(max_length=100, default="Default Wrong Answer 2")
    wrong_answer3 = models.CharField(max_length=100, default="Default Wrong Answer 3")

    def __str__(self):
        return self.question_text

    def check_answer(self, selected_answer):
        # Kiểm tra xem câu trả lời đã chọn có đúng không và trả về kết quả
        return selected_answer == self.correct_answer
class GrammarTest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time_limit_minutes = models.IntegerField()
    number_of_questions = models.IntegerField()

class ReadingTest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time_limit_minutes = models.IntegerField()
    number_of_questions = models.IntegerField()

class WritingTest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time_limit_minutes = models.IntegerField()
    number_of_questions = models.IntegerField()

class ListeningTest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time_limit_minutes = models.IntegerField()
    number_of_questions = models.IntegerField()

class SpeakingTest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time_limit_minutes = models.IntegerField()
    number_of_questions = models.IntegerField()

# class Quiz(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#
# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)  # Thay đổi giá trị mặc định tùy theo ID của bài kiểm tra mặc định
#     content = models.TextField()
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     content = models.CharField(max_length=255)
#     is_correct = models.BooleanField(default=False)

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content

# Định nghĩa Choice
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)


    def __str__(self):
        return self.content + f' {self.is_correct}'


