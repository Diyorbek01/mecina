from django.db.models import fields
from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product, ProductImage, Review
# from .admin import PostAdminForm


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name')

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'category')

@register(ProductImage)
class ProductImageTranslationOptions(TranslationOptions):
    fields = ('product')

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('product', 'comment')