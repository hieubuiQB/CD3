from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("english_learning_app/", include("english_learning_app.urls")),
    path("admin/", admin.site.urls),
]