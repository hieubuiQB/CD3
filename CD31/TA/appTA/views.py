from .forms import LessonForm
from .models import Course, UserProfile, Lesson
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import UserProfile, SessionToken, CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as auth_login
from .models import VocabularyTest, GrammarTest
from .models import Quiz, Question, Choice

def giaodien(request):
    courses = Course.objects.all()
    return render(request, 'giaodien.html', {'courses': courses})

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Đăng ký thành công. Vui lòng đăng nhập.")
            return redirect('login')

    return render(request, 'register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('giaodien')
        else:
            # Xử lý khi xác minh không thành công, ví dụ: hiển thị thông báo lỗi
            return render(request, 'login.html', {'error_message': 'Sai tên đăng nhập hoặc mật khẩu'})

    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def profile(request):
    # Lấy thông tin cá nhân của người dùng đang đăng nhập
    user_profile = UserProfile.objects.all()
    return render(request, 'profile.html', {'user_profile': user_profile})

def user_logout(request):
    logout(request)
    return redirect('giaodien')
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    course = lesson.course  # Lấy khóa học liên quan đến bài học
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)  # Pass the instance for updating
        if form.is_valid():
            form.save()
            messages.success(request, 'Lesson updated successfully.')
            return redirect('lesson_detail', lesson_id=lesson_id)
    else:
        form = LessonForm(instance=lesson)

    return render(request, 'lesson_detail.html', {
        'lesson': lesson,
        'form': form,
        'course': course,
    })


def course_lessons(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lesson_set.all()  # Lấy danh sách bài học của khóa học

    return render(request, 'course_lessons.html', {'course': course, 'lessons': lessons})


def vocabulary_test_list(request):
    # Lấy danh sách các bài kiểm tra từ vựng
    # vocabulary_tests = VocabularyTest.objects.all()
    # return render(request, 'vocabulary_test_list.html', {'vocabulary_tests': vocabulary_tests})
    tests = VocabularyTest.objects.all()
    return render(request, 'vocabulary_test_list.html', {'tests': tests})

def vocabulary_test_detail(request, pk):
    # Lấy thông tin chi tiết của một bài kiểm tra từ vựng
    vocabulary_test = get_object_or_404(VocabularyTest, pk=pk)
    return render(request, 'vocabulary_test_detail.html', {'vocabulary_test': vocabulary_test})

def grammar_test_list(request):
    # Lấy danh sách các bài kiểm tra ngữ pháp
    grammar_tests = GrammarTest.objects.all()
    return render(request, 'grammar_test_list.html', {'grammar_tests': grammar_tests})

def grammar_test_detail(request, pk):
    # Lấy thông tin chi tiết của một bài kiểm tra ngữ pháp
    grammar_test = get_object_or_404(GrammarTest, pk=pk)
    return render(request, 'grammar_test_detail.html', {'grammar_test': grammar_test})

def view_test(request, test_id):
    test = VocabularyTest.objects.get(pk=test_id)
    questions = test.vocabularyquestion_set.all()
    return render(request, 'view_test.html', {'test': test, 'questions': questions})

def view_test(request, test_id):
    test = VocabularyTest.objects.get(pk=test_id)
    questions = test.vocabularyquestion_set.all()
    return render(request, 'view_test.html', {'test': test, 'questions': questions})



def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    context = {
        'quiz': quiz,
        'questions': questions,
    }
    return render(request, 'quiz_detail.html', context)

def quiz_answer(request, quiz_id):
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, id=quiz_id)
        score = 0
        total_questions = 0

        for question in quiz.question_set.all():
            selected_choice_id = request.POST.get(f'question_{question.id}', None)
            if selected_choice_id:
                selected_choice = question.choice_set.get(id=int(selected_choice_id))
                if selected_choice.is_correct:
                    score += 1
            total_questions += 1

        percentage_score = (score / total_questions) * 100

        return render(request, 'quiz_result.html', {'quiz': quiz, 'score': score, 'total_questions': total_questions, 'percentage_score': percentage_score})

    else:
        return redirect('quiz_detail', quiz_id=quiz_id)