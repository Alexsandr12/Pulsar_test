from rest_framework import serializers
from .models import Products


class ProductsFilterSerializers(serializers.ModelSerializer):
    """Сериализатор для проверки передаваемых данных при запросе списка товаров по фильтрам."""
    article = serializers.IntegerField()

    class Meta:
        model = Products
        fields = ["article", "status", "name_product"]


class ProductsSerializers(serializers.ModelSerializer):
    """Сериализатор для формирования ответа."""
    image = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = "__all__"

    def get_image(self, obj):
        image_path_list = str(obj.image).split("/")
        format_img = image_path_list[-1].split(".")[-1]
        name_img = "".join(image_path_list[-1].split(".")[:-1])

        return {
            "path": f"/{'/'.join(image_path_list[:-1])}/{name_img}",
            "formats": [format_img, 'webp'] if format_img in ["jpeg", "jpg", "png"] else [format_img]
        }

    def get_status(self, obj):
        return obj.status.status
