from django import forms,admin
from .models import Product

class ProductAdminForm(forms.ModelForm):
    category = forms.ChoiceField(choices=Product.CATEGORY_CHOICES)

    class Meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('name', 'category', 'price', 'is_available')
