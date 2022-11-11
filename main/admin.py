from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from main.models import Contact, Subscription, Setting, Blog

# Register your models here.
admin.site.register(Subscription)

@admin.register(Contact)
class ManagmentAdmin(TranslationAdmin):
    list_display = ('name', 'subject', 'text')

@admin.register(Blog)
class ManagmentAdmin(TranslationAdmin):
    list_display = ('title', 'description')

@admin.register(Setting)
class ManagmentAdmin(TranslationAdmin):
    list_display = ('name', 'title', 'about_us')

