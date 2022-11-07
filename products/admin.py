from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['sku']
    list_display = [field.name for field in Product._meta.fields if field.name != "id"]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductBrand)
admin.site.register(ProductCategory)
admin.site.register(LowStock)
admin.site.register(StockIn)