from django.urls import path, include
from products.views import (
    ProductListView,
    ProductDetailView
)
from . import views 

urlpatterns = [
    path('', ProductListView.as_view(), name='product-home'),
    path('products/', ProductListView.as_view(), name='p-home'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/', ProductDetailView.as_view(), name='product-detail'),
    path('search/',views.search,name='search' ),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),


]
