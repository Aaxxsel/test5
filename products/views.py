from django.shortcuts import render, get_object_or_404

from products.models import Product


def index(request):
    context = {
        'Title': 'Купить снюс доставкой/самовывоз',
    }

    return render(request, 'products/index.html', context)


def categories(request):
    context = {
        'Title': "Каталог товаров",
        'products': Product.objects.all()
    }
    return render(request, 'products/products.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {'product': product})
