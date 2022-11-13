from modeltranslation.translator import register, TranslationOptions
from product.models import Product, ProductImage, Review, Category


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'category')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name')

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('product', 'comment')