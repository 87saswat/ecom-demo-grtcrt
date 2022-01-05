from django.urls import path
from . import views


urlpatterns=[
    path('', views.store, name='store' ),
    path('category/<slug:category_slug>/', views.store, name='product_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name = 'product_detail'), #url--> store/catregory_slug/product_slug
    path('search/', views.search, name='search'), # url-> 127.0.0.1:8000/store/search/?keyword='searchkeyword'
]