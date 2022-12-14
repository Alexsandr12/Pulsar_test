from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Products
from .serializers import ProductsFilterSerializers, ProductsSerializers


class ProductViewSet(mixins.RetrieveModelMixin,
                     GenericViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers

    @swagger_auto_schema(query_serializer=ProductsFilterSerializers,
                         operation_summary="Поиск продуктов по заданным фильтрам.")
    @action(methods=["get"], detail=False, url_path="filter")
    def products(self, request):
        """Возвращает список продуктов по заданным фильтрам."""
        serializer = ProductsFilterSerializers(data=request.GET, partial=True)
        serializer.is_valid(raise_exception=True,)
        data_req = serializer.validated_data
        products_list = Products.objects.filter(**data_req)

        return Response(ProductsSerializers(products_list, many=True).data)

    @swagger_auto_schema(operation_summary="Поиск продукта по артиклю.")
    def retrieve(self, request, *args, **kwargs):
        """Возвращает продукт по артиклю."""
        return super().retrieve(request, *args, **kwargs)
