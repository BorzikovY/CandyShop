from rest_framework import (
    mixins,
    viewsets, 
    permissions,
)

from logic.models import Candy, Feedback
from api.serializers import (
    CandySerializer, 
    FeedbackSerializer
)


class FeedbackViewSet(
    viewsets.GenericViewSet, 
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    """
    ViewSet отзыва.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.AllowAny]


class CandyViewSet(
    viewsets.GenericViewSet, 
    mixins.ListModelMixin,
):
    """
    ViewSet конфеты.
    """
    queryset = Candy.objects.all()
    serializer_class = CandySerializer
    permission_classes = [permissions.AllowAny]
