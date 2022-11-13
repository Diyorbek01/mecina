import admin_thumbnails
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import Product, ProductImage, Category, Review


@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ('id',)
    extra = 1 

@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'image_thumbnail']



class ProductAdmin(TranslationAdmin):
    list_display = ['title', 'category']
    list_filter = ['category']
    inlines = [ProductImageInline]



# @admin.register(Product)
# class ProductAdminTranslation(TranslationAdmin):
#     list_display = ('title', 'description', 'category')

# @admin.register(Category)
# class CategoryAdminTranslation(TranslationAdmin):
#     list_display = ('name')


# @admin.register(Review)
# class ReviewAdminTranslation(TranslationAdmin):
#     list_display = ('product', 'comment')


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
admin.site.register(Category)
# admin.site.register(ImagesAdmin)