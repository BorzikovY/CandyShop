from rest_framework import (
    mixins,
    viewsets, 
    permissions,
)

from logic.models import (
    Candy,
    Order,
    Feedback, OrderedCandy
)
from api.serializers import (
    CandySerializer,
    OrderSerializer,
    FeedbackSerializer, OrderedCandySerializer,
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


class OrderedCandyViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    """
       ViewSet заказанные конфеты.
    """
    queryset = OrderedCandy.objects.all()
    serializer_class = OrderedCandySerializer
    permission_classes = [permissions.AllowAny]


class OrderViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    """
    ViewSet заказы.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]
