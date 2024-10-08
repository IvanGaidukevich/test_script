from django.contrib import admin
from shop.models import Category, Product
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['available',]
    list_editable = ['price', 'available']