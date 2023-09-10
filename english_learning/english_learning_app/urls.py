# Trong tệp urls.py của ứng dụng của bạn
from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
]
