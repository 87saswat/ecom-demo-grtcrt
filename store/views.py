from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from django.db.models import Q
from category.models import Category
from .models import Product
from cart.models import Cart, CartItem

from django.core.paginator import Page, PageNotAnInteger,Paginator

from cart.views import _cart_id

# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug) # It calls get() on given model manager (Category class here) with slug field, and raises Http404instead ModelDoesnotExist error
        products = Product.objects.filter(category=categories, is_available=True)

         # inititating paginator functionality for "Product categories" with the above query.
        paginator = Paginator(products, 3) 
        page = request.GET.get('page') 
        paged_products = paginator.get_page(page) 

        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('-modified_date')
        
        # inititating paginator functionality for "All Products" with the above query.
        paginator = Paginator(products, 6) # Implementing paginator here, we want to display 6 products in one page
        page = request.GET.get('page') # the "page" parameter will come from the url i.e. we will capture it from 127.0.0.1:8000/store/?page=2 or 127.0.0.1:8000/store/?page=3 etc
        paged_products = paginator.get_page(page) # We got the 6 products per page here and this "paged_products" will be passed in the template
        
        product_count = products.count()

    context= {
    'products': paged_products, 
    'product_count':product_count
    } #Instead of passing total products, we are passing the Paginator's -> paged_product here 


    return render(request,'store.html', context )



def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug = product_slug) #category__slug queries the slug of parent class(Category model) from the category field of the Product class
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product = single_product).exists() #filtered the cart id and product and the exists() returns True or False if the product is available or not

    except Exception as e:
        raise e    
    context={
        'single_product': single_product,
        "in_cart":in_cart
    }
    return render(request,'product-detail.html', context)



def search(request):
    if 'keyword' in request.GET:            #keyword is the name = 'keyword' in our html form
        keyword = request.GET['keyword']    # here we got the value of the keyword e.g url-> https//127.0.0.1:8000/store/search/?keyword='jeans'
        if keyword:
            products = Product.objects.order_by('-modified_date').filter(Q(description__icontains=keyword)| Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {'products': products, 'product_count': product_count}
    return render(request, 'store.html', context)
 