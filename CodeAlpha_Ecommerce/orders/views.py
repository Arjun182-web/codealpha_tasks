from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Order, OrderItem
from cart.models import Cart, CartItem
from django.contrib import messages

@login_required
def checkout(request):

    cart = Cart.objects.get(
        user=request.user
    )

    cart_items = CartItem.objects.filter(
        cart=cart
    )

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    print(total)
    order = Order.objects.create(
        user=request.user,
        total_amount=total
    )

    for item in cart_items:

        OrderItem.objects.create(
        order=order,
        product=item.product,
        quantity=item.quantity,
        price=item.product.price
        )

        product = item.product

        if product.stock >= item.quantity:
            product.stock -= item.quantity
            product.save()

    cart_items.delete()

    messages.success(
    request,
    "Order placed successfully!"
    )
    return render(
        request,
        'orders/success.html',
        {
            'order': order
        }
    )

@login_required
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    )

    return render(
        request,
        'orders/order_history.html',
        {
            'orders': orders
        }
    )