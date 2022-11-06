from django.contrib import admin

from operation.models import OrderProduct, Order, Wishlist


# Register your models here.
class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'status']
    list_filter = ['status']
    can_delete = False
    inlines = [OrderProductline]

    def save_model(self, request, obj, form, change):
        if obj.status == "Completed":
            orderitems = OrderProduct.objects.filter(order_id=obj.id)
            for item in orderitems:
                item.product.amount -= item.quantity
                item.product.count_sold += item.quantity
                item.product.save()
        obj.save()


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']


admin.site.register(Wishlist)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
