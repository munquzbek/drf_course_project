from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course
from users.models import User, Payment, Subscription
from users.serializers import UserSerializer, PaymentSerializer, UserCreateSerializer, SubscriptionSerializer
from users.services import create_stripe_product, create_stripe_price, create_stripe_session


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'type_payment')
    ordering_field = ('-payment_date',)

    def perform_create(self, serializer):
        """overwriting perform create to integrate stripe(payment service)"""
        payment = serializer.save(user=self.request.user)
        product = create_stripe_product(payment.course)
        price = create_stripe_price(product, payment.amount_pay)
        # print(product)
        # print(price)
        session = create_stripe_session(price)
        payment.session = session
        # print(payment.session)
        payment.url = payment.session.get('url')
        payment.save()


class SubscriptionAPIView(APIView):
    """view for subscription to add and to delete subs"""
    serializer_class = SubscriptionSerializer

    def post(self, request):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)

        if Subscription.objects.filter(user=user, course=course_item).exists():
            Subscription.objects.get(user=user, course=course_item).delete()
            message = 'подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'подписка добавлена'

        return Response({"message": message})
