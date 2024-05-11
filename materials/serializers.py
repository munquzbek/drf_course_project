from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='url')]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseLessonSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, source='course', read_only=True)
    has_subs = serializers.SerializerMethodField()

    def get_has_subs(self, course):
        request = self.context.get('request')
        user = None
        if request:
            user = request.user
        return course.subscription_set.filter(user=user).exists()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, instance):
        if instance.course.all().first():
            return instance.course.all().count()
        return 0
