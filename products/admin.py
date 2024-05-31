from django.contrib import admin
from .models import Product, ProductType


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'datedb', 'slug', 'image')
    list_display_links = ('id', 'title')
    ordering = ('-datedb', 'title')
    list_per_page = 4
    search_fields = ['title']
    list_filter = ['datedb', 'title']


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'datedb', 'slug', 'image', 'prod', 'is_active')
    list_display_links = ('id', 'title')
    ordering = ('-datedb', 'title')
    list_per_page = 10
    search_fields = ['title', 'prod__title']
    list_filter = ['datedb', 'title']


