from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from shop.models import CustomUser

@login_required
def customer_list(request):
    user = request.user
    if user.is_authenticated and user.is_staff:  # Only admin can access customer list
        users = CustomUser.objects.all()  # Use the custom user model
        return render(request, 'shop/customer_list.html', {'users': users})
    else:
        return redirect('shop:login')

@login_required
def customer_detail(request, id):
    user = request.user
    if user.is_authenticated and user.is_staff:  # Only admin can access customer detail
        user = get_object_or_404(CustomUser, id=id)  # Use the custom user model
        return render(request, 'shop/customer_detail.html', {'user': user})
    else:
        return redirect('shop:login')

