from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from django.contrib.staticfiles.views import serve
from django.shortcuts import get_object_or_404, redirect
from cart.models import Cart, CartItem


def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'products/home.html', context)

def search(request):
    template = 'products/home.html'
    query = request.GET.get('q')
    result = Product.objects.filter(name__icontains=query)
    context = { 'products': result }
    return render(request, template, context)

def getfile(request):
    return serve(request, 'File')

class ProductListView(ListView):
    model = Product
    template_name = 'products/home.html'
    context_object_name = 'products'
    paginate_by = 10

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    # Check if the user has a cart or create a new one
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Add the product to the cart or update its quantity
    cart_item, item_created = cart.items.get_or_create(product=product)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart:cart')


