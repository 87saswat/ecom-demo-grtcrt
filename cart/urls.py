from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name = 'cart'),
    path('add-cart/<int:product_id>/', views.add_cart, name='add-cart'), #to increment quantity
    path('remove-cart/<int:product_id>/', views.remove_cart, name='remove-cart'),  # to decrement the product quantity            
    path('remove-cart-item/<int:product_id>/', views.remove_cart_item, name='remove-cart-item')
]