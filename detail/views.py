from django.shortcuts import render, get_object_or_404
from detail.models import Product
# Create your views here.

def detail_top(request):
    product = Product.objects.all()
    top = Product.objects.filter(category='1')
    return render(request, 'detail/detail_top.html', {'product': product, 'top':top})

def detail_bottom(request):
    product = Product.objects.all()
    bottom = Product.objects.filter(category='2')
    return render(request, 'detail/detail_bottom.html', {'product': product, 'bottom':bottom})


def detail_product(request, id):
    detail_product = get_object_or_404(Product, pk=id)
    return render(request, 'detail/detail_product.html', {'detail_product':detail_product})