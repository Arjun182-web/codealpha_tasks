from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Wishlist
from products.models import Product
from django.contrib import messages

@login_required
def add_to_wishlist(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )
    messages.success(
    request,
    "Added to wishlist ❤️"
    )
    return redirect('/')

@login_required
def wishlist_view(request):

    items = Wishlist.objects.filter(
        user=request.user
    )

    return render(
        request,
        'wishlist/wishlist.html',
        {
            'items': items
        }
    )

@login_required
def remove_wishlist(request, item_id):

    item = Wishlist.objects.get(
        id=item_id,
        user=request.user
    )

    item.delete()
    messages.warning(
    request,
    "Removed from wishlist"
    )
    return redirect('/wishlist/')