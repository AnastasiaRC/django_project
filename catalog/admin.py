from django.contrib import admin
from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_product', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('title_product', 'description_product')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_category',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "version_number", "version_name", "is_active")
    list_filter = ('product',)
