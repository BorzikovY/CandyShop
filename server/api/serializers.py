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
    candies = SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'address', 'price', 'candies')

    def get_candies(self, obj) -> list[OrderedCandySerializer]:
        return OrderedCandySerializer(
            OrderedCandy.objects.filter(order=obj),
            many=True
        ).data


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"

