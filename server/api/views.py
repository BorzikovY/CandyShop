from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework import (
    mixins,
    viewsets,
    permissions, status,
)
from rest_framework.decorators import action
from rest_framework.response import Response

from logic.geolocation import generate_coordinates
from logic.models import (
    Candy,
    Order,
    Feedback, OrderedCandy
)
from api.serializers import (
    CandySerializer,
    OrderSerializer,
    FeedbackSerializer, OrderedCandySerializer, OrderedCandyCreateSerializer, OrderCoordinatesSerializer,
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
):
    """
    ViewSet для работы с заказами.

    list: Получение списка заказов
    create_order: Создание нового заказа с конфетами
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=OrderedCandyCreateSerializer(many=True),
        responses={
            201: OrderCoordinatesSerializer,
            400: "Невалидные данные",
            500: "Ошибка сервера"
        },
        operation_description="Создание нового заказа с конфетами",
        operation_summary="Создание заказа"
    )
    @action(detail=False, methods=['post'], url_path='create-order')
    def create_order(self, request):
        """
        Создание заказа с указанными конфетами.

        Принимает список конфет в формате:
        [{"candy_id": 1, "weight": 100}, ...]

        Возвращает координаты созданного заказа.
        """
        ordered_candies_data = request.data

        if not isinstance(ordered_candies_data, list):
            return Response(
                {'error': 'Expected list of ordered candies'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = OrderedCandyCreateSerializer(
            data=ordered_candies_data,
            many=True
        )

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                ordered_candies = serializer.save()
                coordinates = generate_coordinates("Москва", 1)[0]

                order = Order.objects.create(
                    latitude=round(coordinates[0], 8),
                    longitude=round(coordinates[1], 8)
                )
                order.candies.set(ordered_candies)

                return Response({
                    'latitude': float(order.latitude),
                    'longitude': float(order.longitude)
                }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
