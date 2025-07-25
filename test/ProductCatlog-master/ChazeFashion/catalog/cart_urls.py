from django.urls import path
from catalog.views import (
    add_to_cart,
    cart,
    remove_from_cart,
    update_cart_item,
    move_to_wishlist,
)

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('', cart, name='view_cart'),  # this replaces view_cart
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update/<int:product_id>/', update_cart_item, name='update_cart_item'),
    path('move-to-wishlist/<int:item_id>/', move_to_wishlist, name='move_to_wishlist'),
]
