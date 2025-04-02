from rest_framework.serializers import ModelSerializer
from logic.models import Candy, Feedback


class CandySerializer(ModelSerializer):
    class Meta:
        model = Candy
        fields = "__all__"


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"

