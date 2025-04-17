from rest_framework.fields import SerializerMethodField, IntegerField, FloatField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, Serializer
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


class OrderedCandyCreateSerializer(ModelSerializer):
    candy_id = PrimaryKeyRelatedField(
        source='candy',
        queryset=Candy.objects.all()
    )
    weight = IntegerField(min_value=1)

    class Meta:
        model = OrderedCandy
        fields = ('candy_id', 'weight')


class OrderCoordinatesSerializer(Serializer):
    latitude = FloatField()
    longitude = FloatField()
