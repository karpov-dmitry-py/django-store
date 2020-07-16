from django.urls import path
from . import views as store_views

urlpatterns = [
    path('', store_views.store, name='store'),
    path('cart/', store_views.cart, name='cart'),
    path('checkout/', store_views.checkout, name='checkout'),
]