from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from materials.models import Course, Lesson
from materials.paginators import CoursePaginator
from materials.serializers import CourseSerializer, LessonSerializer, CourseLessonSerializer
from users.permissions import IsModer, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def get_serializer_class(self):
        if self.action == "post":
            return CourseSerializer
        return CourseLessonSerializer

    def get_permissions(self):
        """setting permission for moders to update and retrieve only, moders cant create or delete"""
        if self.action == "create":
            self.permission_classes = (~IsModer,)
        elif self.action in ["update", "retrieve", "partial_update"]:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModer | IsOwner,)
        return super().get_permissions()

    def perform_create(self, serializer):
        """auto adding to course its owner who create course"""
        course = serializer.save()
        course.owner = self.request.user
        course.save()


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    """if user is in moders group he cant create new lessons"""
    permission_classes = [~IsModer]

    def perform_create(self, serializer):
        """auto adding to lesson its owner who create lesson"""
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    """if user is in moders group he can view full list lessons"""
    permission_classes = [IsModer | IsOwner]
    pagination_class = CoursePaginator


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    """if user is in moders group he can view lessons"""
    permission_classes = [IsModer | IsOwner]


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    """if user is in moders group he can update lessons"""
    permission_classes = [IsModer | IsOwner]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    """if user is in moders group he cant delete lessons"""
    permission_classes = [~IsModer | IsOwner]
