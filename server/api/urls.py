from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.views import (
   CandyViewSet,
   FeedbackViewSet, OrderViewSet, OrderedCandyViewSet,
)


schema_view = get_schema_view(
   openapi.Info(
      title="CandyShop API",
      default_version='v1',
      description="api docs",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   url="http://127.0.0.1:8000",
)

router = DefaultRouter()
router.register('candies', CandyViewSet, basename='candy')
router.register('ordered_candies', OrderedCandyViewSet, basename='ordered_candy')
router.register('orders', OrderViewSet, basename='order')
router.register('feedbacks', FeedbackViewSet, basename='feedback')

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('', include(router.urls)),
]
