from django.shortcuts import render, get_object_or_404
from shop.models import Product, Banner
from django.db.models import Max, Min

# Create your views here.

def index(request):
    banner = Banner.objects.all()
    product = Product.objects.all()
    new = Product.objects.last()
    best = Product.objects.all().order_by('-hit')[0]
    sold_out = Product.objects.all().order_by('quantity')[0]
    return render(request, 'shop/index.html', {'new': new, 'best':best, 'sold_out':sold_out, 'banner':banner, 'product':product})

def index_product(request,id):
    index_product = get_object_or_404(Product, pk=id)
    return render(request, 'shop/index_product.html', {'index_product':index_product})

