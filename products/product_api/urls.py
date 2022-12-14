from django.urls import path, include
from rest_framework import routers

from .views import ProductViewSet

router = routers.DefaultRouter()
router.register("product", ProductViewSet, basename="product")


app_name = "product_api"
urlpatterns = [
    path('', include(router.urls))
]
