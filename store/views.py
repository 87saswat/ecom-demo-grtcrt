from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product

# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug) # It calls get() on given model manager (Category class here) with slug field, and raises Http404instead ModelDoesnotExist error
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context= {
    'products': products, 
    'product_count':product_count
    }


    return render(request,'store.html', context )



def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug = product_slug) #category__slug queries the slug of parent class(Category model) from the category field of the Product class
    except Exception as e:
        raise e    
    context={
        'single_product': single_product
    }
    return render(request,'product-detail.html', context)