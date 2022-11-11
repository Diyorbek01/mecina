from modeltranslation.translator import register, TranslationOptions
from .models import Contact, Blog, Setting


@register(Contact)
class ManagmentTranslationOptions(TranslationOptions):
    fields = ('name', 'subject', 'text')


@register(Blog)
class SectionsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Setting)
class SectionsTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'about_us')