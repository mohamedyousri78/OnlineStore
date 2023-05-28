from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='cart'),
    #path('cart/', views.view_cart, name='cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    # Other URL patterns for adding/removing items, updating quantities, etc .
]
