from django.db import models
from .myfields import WEBPField


class Products(models.Model):
    article = models.PositiveIntegerField(unique=True)
    name_product = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = WEBPField(upload_to="images/product/")
    status = models.ForeignKey("StatusProduct", on_delete=models.PROTECT, related_name='product')

    def __str__(self):
        return f"{self.article}-{self.name_product}"

    class Meta:
        verbose_name_plural = "Products"


class StatusProduct(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = "StatusProduct"
