from django.contrib import admin

from main.models import Contact, Subscription, Setting, Blog

# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Subscription)
admin.site.register(Setting)
