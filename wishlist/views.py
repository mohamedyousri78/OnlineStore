from django.shortcuts import render, get_object_or_404, redirect
from .models import Wishlist, WishlistItem
from django.contrib.auth.decorators import login_required
from products.models import Product

@login_required
def view_wishlist(request):
    wishlist_items = WishlistItem.objects.filter(wishlist__user=request.user)

    context = {
        'wishlist_items': wishlist_items,
    }

    return render(request, 'wishlist/wishlist.html', context)

@login_required
def add_to_wishlist(request, product_id):
    try:
        wishlist = request.user.wishlist
    except Wishlist.DoesNotExist:
        wishlist = Wishlist.objects.create(user=request.user)

    if wishlist.items.filter(product_id=product_id).exists():
        # Item already exists in the wishlist
        return redirect('wishlist:wishlist')

    product = get_object_or_404(Product, pk=product_id)
    WishlistItem.objects.create(wishlist=wishlist, product=product)

    return redirect('wishlist:wishlist')

@login_required
def remove_from_wishlist(request, item_id):
    item = get_object_or_404(WishlistItem, pk=item_id)
    item.delete()
    return redirect('wishlist:wishlist')
