from django.contrib import admin

from .models import Products, StatusProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ("article", "name_product", "price", "image", "status_id")
    fields = ("article", "name_product", "price", "image", "status")


class StatusProductAdmin(admin.ModelAdmin):
    list_display = ("status",)
    fields = ("status",)


admin.site.register(Products, ProductAdmin)
admin.site.register(StatusProduct, StatusProductAdmin)
