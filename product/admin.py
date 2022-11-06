import admin_thumbnails
from django.contrib import admin

from product.models import Product, ProductImage, Category, Review


@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ('id',)
    extra = 1


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'image_thumbnail']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['category']
    inlines = [ProductImageInline]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ImagesAdmin)
admin.site.register(Category)
admin.site.register(Review)
