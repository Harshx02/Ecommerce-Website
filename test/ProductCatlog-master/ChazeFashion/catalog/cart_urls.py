from django.urls import path
from catalog.views import (
    add_to_cart,
    cart,
    remove_from_cart,
)

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
 path('', cart, name='view_cart'),  # this replaces view_cart
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]
