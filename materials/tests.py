from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    """testcase for CRUD all lesson view"""

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.com",
            password='12345'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title="TestCourse",
            description="TestCourse"
        )
        self.lesson = Lesson.objects.create(
            title="TestLesson",
            description="TestLesson",
            course=self.course,
            owner=self.user
        )

    def test_list_lesson(self):
        response = self.client.get(
            '/lms/lesson/list',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        print(response.json())
        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 5, 'title': 'TestLesson', 'description': 'TestLesson', 'preview': None, 'url': None, 'course': 4,
                 'owner': 4}]}

        )

    def test_create_lesson(self):
        data = {
            "title": self.lesson.title,
            "description": self.lesson.description,
            "course": self.course.id,
            "url": "https://www.youtube.com/",
        }
        response = self.client.post(
            '/lms/lesson/create',
            data=data
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )
        # print(Lesson.objects.all().exists())
        # print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_detail_lesson(self):
        data = {
            "title": self.lesson.title,
            "description": self.lesson.description,
        }
        response = self.client.get(f'/lms/lesson/view/{self.lesson.id}', data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):
        data = {
            'title': 'TestUpdateLesson',
            'description': 'TestUpdateLesson',
            'course': self.course.id,
            'owner': self.user.id,
            "url": "https://www.youtube.com/",
        }
        response = self.client.patch(
            f'/lms/lesson/update/{self.lesson.id}',
            data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.lesson.refresh_from_db()

        self.assertEqual(
            self.lesson.title,
            data['title']
        )
        self.assertEqual(
            self.lesson.description,
            data['description']
        )

    def test_delete_lesson(self):
        data = {
            'title': 'delete test',
            'description': 'delete test',
        }
        response = self.client.delete(
            f'/lms/lesson/delete/{self.lesson.id}',
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
