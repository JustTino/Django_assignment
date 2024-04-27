from django.urls import path, include
from . import views
from shop.views import products, customers, orders, basket, general
from .views.general import payment_success
import django.contrib.auth.urls


app_name = 'shop'

# Define a separate URL patterns list for admin-only paths
admin_urlpatterns = [
    path('', products.product_list, name='product_list'),
    path('product/<int:id>/delete/', views.products.product_delete, name='product_delete'),
    path('product/<int:id>/edit/', views.products.product_edit, name='product_edit'),
    path('product_list/', products.product_list, name='product_list'),
    path('product_detail/<int:id>/', products.product_detail, name='product_detail'),
    path('product_new/', products.product_new, name='product_new'),
]

# Define the admin_urls function to conditionally include admin-only paths
def admin_urls(request):
    if request.user.is_authenticated and request.user.is_staff:
        return admin_urlpatterns
    return []

urlpatterns = [
    # Paths accessible to all users
    path('', products.product_list, name='product_list'),
    path('product/<int:id>/delete/', views.products.product_delete, name='product_delete'),
    path('product/<int:id>/edit/', views.products.product_edit, name='product_edit'),
    path('product_list/', products.product_list, name='product_list'),
    path('product_detail/<int:id>/', products.product_detail, name='product_detail'),
    path('product_new/', products.product_new, name='product_new'),
    path('', products.product_list, name='product_list'),
    path('signup/', views.general.signup, name='signup'),
    path('basket_add/<int:product_id>/', views.basket.basket_add, name='basket_add'),
    path('basket_remove/<int:product_id>/', views.basket.basket_remove, name='basket_remove'),
    path('basket_detail/', views.basket.basket_detail, name='basket_detail'),
    path('payment/', views.general.payment, name='payment'),
    path('login/', views.general.login_view, name='login'),

    # Paths accessible only to authenticated users
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.general.dashboard, name='dashboard'),
    path('payment/', views.general.payment, name='payment'),
    path('customer_list/', views.customers.customer_list, name='customer_list'),
    path('customer/<int:id>/', views.customers.customer_detail, name='customer_detail'),
    path('order_list/', views.orders.order_list, name='order_list'),
    path('order/<int:id>/', views.orders.order_detail, name='order_detail'),
    path('payment/success/', payment_success, name='payment_success'),

    # Include admin-only paths by calling the admin_urls function
    path('admin/', admin_urls),
]


# from django.urls import path, include
# import django.contrib.auth.urls
# from . import views
# from shop.views import products, customers, orders, basket, general
# from django.urls import path
# from .views.general import payment_success





# app_name = 'shop'

# # Define a separate URL patterns list for admin-only paths
# admin_urlpatterns = [
#     path('', products.product_list, name='product_list'),
#      path('product/<int:id>/delete/', views.products.product_delete, name='product_delete'),
#     path('product/<int:id>/edit/', views.products.product_edit, name='product_edit'),
#     path('product_list/', products.product_list, name='product_list'),
#     path('product_detail/<int:id>/', products.product_detail, name='product_detail'),
#     path('product_new/', products.product_new, name='product_new'),
#       # Include product_detail here
    
# ]

# # Define the admin_urls function to conditionally include admin-only paths
# def admin_urls(request):
#     if request.user.is_authenticated and request.user.is_staff:
#         return admin_urlpatterns
#     return []

# urlpatterns = [
#     # Paths accessible to all users
#    path('', products.product_list, name='product_list'),
#      path('product/<int:id>/delete/', views.products.product_delete, name='product_delete'),
#     path('product/<int:id>/edit/', views.products.product_edit, name='product_edit'),
#     path('product_list/', products.product_list, name='product_list'),
#     path('product_detail/<int:id>/', products.product_detail, name='product_detail'),
#     path('product_new/', products.product_new, name='product_new'),
#     path('', products.product_list, name='product_list'),
#     path('signup/', views.general.signup, name='signup'),
#     path('basket_add/<int:product_id>/', views.basket.basket_add, name='basket_add'),
#     path('basket_remove/<int:product_id>/', views.basket.basket_remove, name='basket_remove'),
#     path('basket_detail/', views.basket.basket_detail, name='basket_detail'),
#     # path('payment/', views.general.purchase, name='payment'),
#     path('payment/', views.general.payment, name='payment'),
#     path('login/', views.general.login_view, name='login'),

#     # Paths accessible only to authenticated users
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('dashboard/', views.general.dashboard, name='dashboard'),
#     path('payment/', views.general.payment, name='payment'),
#     path('customer_list/', views.customers.customer_list, name='customer_list'),
#     path('customer/<int:id>/', views.customers.customer_detail, name='customer_detail'),
#     path('order_list/', views.orders.order_list, name='order_list'),
#     path('order/<int:id>/', views.orders.order_detail, name='order_detail'),
#     path('payment/success/', payment_success, name='payment_success'),
    

#     # Include admin-only paths by calling the admin_urls function
#     # path('', admin_urls),
#     path('admin/', admin_urls),
# ]
