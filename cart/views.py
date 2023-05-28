from django.shortcuts import render
from .models import Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import CartItem

@login_required
def view_cart(request):
    # Retrieve the user's cart if available
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
    except Cart.DoesNotExist:
        cart = None
        cart_items = []

    context = {
        'cart': cart,
        'cart_items': cart_items
    }

    return render(request, 'cart/cart.html', context)

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id)
    item.delete()
    return redirect('cart:cart')



