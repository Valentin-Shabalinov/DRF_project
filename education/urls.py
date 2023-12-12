from django.urls import path
from rest_framework.routers import DefaultRouter
from education.apps import EducationConfig
from education.views import (
    CourseViewSet,
    LessonListView,
    LessonDetailView,
    LessonCreateView,
    LessonUpdateView,
    LessonDeleteView,
)

app_name = EducationConfig.name

router = DefaultRouter()
router.register("course", CourseViewSet, basename="course")

urlpatterns = [
    path("lesson/", LessonListView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonDetailView.as_view(), name="lesson_detail"),
    path(
        "lesson/update/<int:pk>/",
        LessonUpdateView.as_view(),
        name="lesson_update",
    ),
    path("lesson/create/", LessonCreateView.as_view(), name="lesson_create"),
    path(
        "lesson/delete/<int:pk>/",
        LessonDeleteView.as_view(),
        name="lesson_delete",
    ),
] + router.urls
