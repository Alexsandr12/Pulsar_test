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

    # @swagger_auto_schema(query_serializer=VpsSerializers,
    #                      operation_summary="Получение списка VPS-серверов по заданным фильтрам.",
    #                      operation_description=status_desc)
    @action(methods=["get"], detail=False, url_path="filter")
    def products(self, request):
        """Поиск продуктов по заданным фильтрам."""
        serializer = ProductsFilterSerializers(data=request.GET, partial=True)
        serializer.is_valid(raise_exception=True,)
        data_req = serializer.validated_data
        products_list = Products.objects.filter(**data_req)

        return Response(ProductsSerializers(products_list, many=True).data)

    def retrieve(self, request, *args, **kwargs):
        """Возвращает VPS-сервер по uid."""
        return super().retrieve(request, *args, **kwargs)
