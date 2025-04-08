from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from logic.models import Candy, Order, OrderedCandy, Feedback


class CandySerializer(ModelSerializer):
    class Meta:
        model = Candy
        fields = "__all__"


class OrderedCandySerializer(ModelSerializer):
    candy = CandySerializer(many=False)

    class Meta:
        model = OrderedCandy
        fields = ('id', 'candy', 'weight')


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'latitude', 'longitude', 'price', 'candies')


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"
