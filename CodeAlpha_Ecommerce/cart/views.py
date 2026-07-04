from django.shortcuts import get_object_or_404, redirect , render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Cart, CartItem
from products.models import Product

@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    if product.stock <= 0:

        messages.error(
            request,
            "Product is out of stock."
        )

        return redirect('/')

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(
    request,
    f"{product.name} added to cart Successfully!"
    )
    return redirect('/')


@login_required
def cart_view(request):

    print("Current User:", request.user)

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_items = CartItem.objects.filter(
        cart=cart
    )

    for item in cart_items:
        item.subtotal = item.product.price * item.quantity


    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    return render(
    request,
    'cart/cart.html',
    {
        'cart_items': cart_items,
        'total': total
    }
    )

@login_required
def remove_from_cart(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    item.delete()

    return redirect('cart')

@login_required
def increase_quantity(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    item.quantity += 1
    item.save()

    return redirect('cart')


@login_required
def decrease_quantity(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart')