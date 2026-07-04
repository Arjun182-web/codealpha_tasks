from django.contrib import admin
from .models import Cart, CartItem

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        'get_user',
        'product',
        'quantity',
    )

    def get_user(self, obj):
        return obj.cart.user.username

    get_user.short_description = "User"

admin.site.register(Cart)