from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from store.models import Product
from cart.models import Cart, CartItem


# Create your views here.
# we will use the session id from the browser and save it to the database as cart id


def _cart_id(request):
    cart = request.session.session_key #getting the session key from request object
    if not cart:
        cart = request.session.create () #If no session id present then we will create a new session id
    return cart    





def add_cart(request, product_id):
    product = Product.objects.get(id = product_id)           #get the product using the product's id   
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))  #passing the above function which returns a session key
    except Cart.DoesNotExist:                                # If cart doesnot exists, we will create a cart
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()    

    try:                                                    # One cart contains many product, so we are creating a functionality to add products to the cart
        cart_item = CartItem.objects.get(product = product, cart = cart) # brings product and cart together
        cart_item.quantity +=1                              # Increased the quantity by 1 whenever product added
        cart_item.save()
    except CartItem.DoesNotExist:                         #If CartItem is not there, create a new one
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,

        )   
        cart_item.save() 
    return redirect('cart')    



def cart(request, total = 0, quantity = 0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True) # we got all the items addd inside the cart
        for cart_item in cart_items:
            total = total+ (cart_item.product.price * cart_item.quantity) #total initially set to 0, and here we are adding Product.price * quantity to get the total amount
            quantity +=cart_item.qunatity                                 #quantity initialyy set to 0, here we are getting the quntity from the cart 
    except ObjectDoesNotExist:
        pass        

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items 
    }
    return render(request, 'cart.html', context)        