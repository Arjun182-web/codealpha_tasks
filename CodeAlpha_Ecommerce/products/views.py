from django.shortcuts import render, get_object_or_404
from .models import Product,Category
from django.core.paginator import Paginator

def product_list(request):
    categories = Category.objects.all()

    category_id = request.GET.get('category')

    products = Product.objects.all()

    sort = request.GET.get('sort')

    query = request.GET.get('q')

    if query:
        products = products.filter(
        name__icontains=query
        )

    if category_id:
        products = products.filter(
            category_id=category_id
            )
    if sort == 'low':
        products = products.order_by('price')

    elif sort == 'high':
        products = products.order_by('-price')

    elif sort == 'new':
        products = products.order_by('-created_at')

    paginator = Paginator(products, 6)

    page_number = request.GET.get('page')

    products = paginator.get_page(page_number)
        
    return render(
        request,
        'products/product_list.html',
        {'products': products ,
         'categories': categories}
        )

def product_detail(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id
    )

    return render(
        request,
        'products/product_detail.html',
        {'product': product}
    )

