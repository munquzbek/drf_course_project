from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Course
from users.models import User


class SubscriptionTesCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # create user in test database
        self.user = User.objects.create(id=1, email='test@test.test', password=12345)
        self.client.force_authenticate(user=self.user)
        # create test course
        self.course = Course.objects.create(id=1, title='TestCourse', description='TestCourse')

    def test_has_subs_on(self):
        """Test has subs"""
        data = {
            'user': self.user.id,
            'course': self.course.id
        }
        response = self.client.post('/users/subs/', data=data)
        # print(response.json())
        # print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "подписка добавлена")

    def test_has_subs_off(self):
        """Test doesnt have subs(two request add subs and delete)"""
        data = {
            'user': self.user.id,
            'course': self.course.id
        }
        response = self.client.post('/users/subs/', data=data)
        response = self.client.post('/users/subs/', data=data)
        # print(response.json())
        # print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "подписка удалена")
