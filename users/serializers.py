from rest_framework import serializers

from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    country = serializers.CharField()  # You can add extra fields to a ModelSerializer or override the default fields
    # by declaring fields on the class, just as you would for a Serializer class.
    payment = PaymentSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
