from django.contrib import admin
from .models import Category, Product 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_feilds = {'slug': ('name',)}
    list_display = ['name', 'slug']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'instock', 'created', 'updated']
    list_filter = ['instock', 'isactive']
    list_editable = ['price', 'instock']
    prepopulated_feilds = {'slug': ('title',)}

