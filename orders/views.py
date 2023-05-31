from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from .forms import OrderForm
from cart.models import CartItem
@login_required
def create_order(request):
    order_price = 0  # Initialize order_price variable
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cart_items = CartItem.objects.filter(cart__user=request.user)
            for item in cart_items:
                order_price += (item.product.price * item.quantity)
            
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = order_price  # Set the total_price field
            print(order.total_price)
            order.save()
            
            for item in cart_items:
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)
            cart_items.delete()
            
            return redirect('orders:order_detail', order_id=order.pk)
    else:
        cart_items = CartItem.objects.filter(cart__user=request.user)
        for item in cart_items:
            order_price += (item.product.price * item.quantity)        
        form = OrderForm(initial={'total_price': order_price})  # Set initial value for total_price field
    
    return render(request, 'orders/create_order.html', {'form': form, 'order_price': order_price})


@login_required
def order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    order_items = order.items.all()
    return render(request, 'orders/order_detail.html', {'order': order, 'order_items': order_items})

@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/user_orders.html', {'orders': orders})