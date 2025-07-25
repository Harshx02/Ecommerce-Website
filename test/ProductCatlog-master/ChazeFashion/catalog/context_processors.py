from .models import Cart, CartItem

def cart(request):
    """Provide cart context for all templates"""
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_items = cart.items.all()
            cart_count = sum(item.quantity for item in cart_items)
            cart_total = sum(item.product.pr_price * item.quantity for item in cart_items)
        except Cart.DoesNotExist:
            cart_count = 0
            cart_total = 0
            cart_items = []
    else:
        cart_count = 0
        cart_total = 0
        cart_items = []
    
    return {
        'cart_count': cart_count,
        'cart_total': cart_total,
        'cart_items': cart_items
    }