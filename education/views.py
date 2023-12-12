from rest_framework.generics import (
    RetrieveAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    CreateAPIView,
)

from education.models import Course, Lesson

from education.serializers import (
    CourseSerializer,
    LessonSerializer,
    LessonDetailSerializer,
    LessonListSerializer,
)

from rest_framework.viewsets import ModelViewSet


class CourseViewSet(ModelViewSet):
    """Viewset for course"""

    serializer_class = CourseSerializer

    queryset = Course.objects.all()


class LessonListView(ListAPIView):
    """Lesson list API View"""

    serializer_class = LessonListSerializer
    queryset = Lesson.objects.all()


class LessonDetailView(RetrieveAPIView):
    """Lesson detail API View"""

    serializer_class = LessonDetailSerializer
    queryset = Lesson.objects.all()


class LessonCreateView(CreateAPIView):
    """Lesson create API View"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateView(UpdateAPIView):
    """Lesson update API View"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteView(DestroyAPIView):
    """Lesson delete API View"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
