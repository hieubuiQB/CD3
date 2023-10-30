# Trong tệp urls.py của ứng dụng của bạn
from django.urls import path
from . import views

urlpatterns = [
    path('', views.giaodien, name='giaodien'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('course/<int:course_id>/lessons/', views.course_lessons, name='course_lessons'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('vocabulary-tests/', views.vocabulary_test_list, name='vocabulary_test_list'),

    # URL cho chi tiết bài kiểm tra từ vựng (truyền pk làm tham số)
    path('vocabulary-tests/<int:pk>/', views.vocabulary_test_detail, name='vocabulary_test_detail'),

    # URL cho danh sách bài kiểm tra ngữ pháp
    path('grammar-tests/', views.grammar_test_list, name='grammar_test_list'),

    # URL cho chi tiết bài kiểm tra ngữ pháp (truyền pk làm tham số)
    path('grammar-tests/<int:pk>/', views.grammar_test_detail, name='grammar_test_detail'),

    path('quiz/', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/answer/', views.quiz_answer, name='quiz_answer'),
]