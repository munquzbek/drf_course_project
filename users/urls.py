from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, UserListAPIView, PaymentViewSet, UserCreateAPIView, UserDestroyAPIView, \
    UserRetrieveAPIView, SubscriptionAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [
                  # Subscription
                  path('subs/', SubscriptionAPIView.as_view(), name='subs'),

                  # token for user
                  path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

                  # user
                  path('register/', UserCreateAPIView.as_view(), name='profile-register'),
                  path('view/<int:pk>/', UserRetrieveAPIView.as_view(), name='profile-view'),
                  path('list/', UserListAPIView.as_view(), name='profile-list'),
                  path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='profile-update'),
                  path('destroy/<int:pk>/', UserDestroyAPIView.as_view(), name='profile-destroy'),
              ] + router.urls
