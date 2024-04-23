from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, UserListAPIView, PaymentViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [
    # user
    path('list/', UserListAPIView.as_view(), name='profile-list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='profile-update')
] + router.urls
