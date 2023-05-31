from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('user_orders/', views.user_orders, name='user_orders'),
]