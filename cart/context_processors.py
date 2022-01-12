from .models import CartItem, Cart
from .views import _cart_id



# To get the number of items in our cart
def counter(request):
    cart_count=0
    if 'admin' in request.path:     #if we are inside admin, then we dont want to see anything, so returning an empty dict.
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id = _cart_id(request))  #bring the cart id (which is the session key)
            cart_items = CartItem.objects.all().filter(cart=cart[:1]) #filter it and we only need one result thats why cart[:1]
            for cart_item in cart_items:
                cart_count += cart_item.quantity                    #we are getting the quantity of from CartItem.quantity (in models)
        except Cart.DoesNotExist:
            cart_count=0
    return dict(cart_count=cart_count)            