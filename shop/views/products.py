from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from shop.forms import BasketAddProductForm, ProductForm
from shop.models import Product
from django.db.models import Q
from django.contrib import messages

def product_list(request):
    products = Product.objects.all()
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(brand__icontains=query) |
            Q(model__icontains=query) |
            Q(product_type__icontains=query)
        )
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    basket_product_form = BasketAddProductForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'basket_product_form': basket_product_form})

# def product_new(request):
#     if request.user.is_authenticated and request.user.is_staff:
#         if request.method == "POST":
#             form = ProductForm(request.POST)
#             if form.is_valid():
#                 product = form.save(commit=False)
#                 product.created_date = timezone.now()
#                 product.save()
#                 return redirect('shop:product_detail', id=product.id)
#         else:
#             form = ProductForm()
#         return render(request, 'shop/product_edit.html', {'form': form})
#     else:
#         return redirect('shop:login')
def product_new(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == "POST":
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.created_date = timezone.now()
                product.save()
                return redirect('shop:product_detail', id=product.id)
        else:
            form = ProductForm()
        return render(request, 'shop/product_edit.html', {'form': form})
    else:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('shop:product_list')

def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == "POST":
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                product = form.save(commit=False)
                product.created_date = timezone.now()
                product.save()
                return redirect('shop:product_detail', id=product.id)
        else:
            form = ProductForm(instance=product)
        return render(request, 'shop/product_edit.html', {'form': form})
    else:
        return redirect('shop:login')

def product_delete(request, id):
    if request.user.is_authenticated and request.user.is_staff:
        product = get_object_or_404(Product, id=id)
        deleted = request.session.get('deleted', 'empty')
        request.session['deleted'] = product.name
        product.delete()
        return redirect('shop:product_list')
    else:
        return redirect('shop:login')
