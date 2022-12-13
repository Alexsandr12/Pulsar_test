from django.db import models


class Products(models.Model):
    article = models.PositiveIntegerField(unique=True)
    name_product = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2)
    image = models.ImageField(upload_to="images/product/")
    status = models.ForeignKey("StatusProduct", on_delete=models.PROTECT, related_name='product')

    class Meta:
        verbose_name_plural = "Products"


class StatusProduct(models.Model):
    status = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "StatusProduct"
