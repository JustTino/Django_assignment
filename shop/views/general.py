from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from shop.forms import SignUpForm
from shop.models import Cart, Customer, LineItem, Order, Product
from shop.views.basket import Basket
from shop.models import CustomUser
from django.shortcuts import render
from shop.models import Order, LineItem
from django.http import Http404
from shop.forms import PaymentForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render, get_object_or_404

# def signup(request):
#     form = SignUpForm(request.POST)
#     if form.is_valid():
#         user = form.save()
#         user.refresh_from_db()
#         user.customer.first_name = form.cleaned_data.get('first_name')
#         user.customer.last_name = form.cleaned_data.get('last_name')
#         user.customer.address = form.cleaned_data.get('address')
#         user.save()
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password= password)
#         login(request, user)
#         return redirect('/')
#     return render(request, 'signup.html', {'form': form})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.customer = Customer.objects.create(user=user, address=form.cleaned_data.get('address'))
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('product_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    if user.is_authenticated and user.is_staff:
        return render(request, 'shop/dashboard.html')
    else:
        return redirect('shop:login')
        


def payment(request):
    if request.method == 'POST':
        # Assuming you have a form to submit payment details
        # Process payment details here
        basket = Basket(request)
        user = request.user
        customer = get_object_or_404(Customer, user=user)
        order = Order.objects.create(customer=customer)
        order.refresh_from_db()
        for item in basket:
            product_item = get_object_or_404(Product, id=item['product_id'])
            cart = Cart.objects.create(product=product_item, quantity=item['quantity'])
            cart.refresh_from_db()
            line_item = LineItem.objects.create(quantity=item['quantity'], product=product_item, cart=cart, order=order)

        basket.clear()
        request.session['deleted'] = 'thanks for your purchase'
        return redirect('shop:payment_success')
    else:
        return redirect('shop:payment_success')

def payment_success(request):
    user = request.user
    customer = get_object_or_404(Customer, user=user)
    order = Order.objects.filter(customer=customer).last()  # Get the latest order for the customer
    if not order:
        raise Http404("No orders found")
    order_items = LineItem.objects.filter(order=order)
    total_amount = sum(item.product.price * item.quantity for item in order_items)
    delivery_address = customer.address
    return render(request, 'shop/payment_success.html', {'order_items': order_items, 'total_amount': total_amount, 'delivery_address': delivery_address})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('product_list')
    else:
        return redirect('login')
