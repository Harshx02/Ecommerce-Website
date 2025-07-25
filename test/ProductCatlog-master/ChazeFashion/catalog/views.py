from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product, UserProfile, Cart, Wishlist, Order, CartItem
from .forms import UserProfileForm

def home(request):
    """Home/Landing page"""
    products = Product.objects.all()[:8]  # Show first 8 products
    context = {
        'products': products,
    }
    return render(request, 'catalog/home.html', context)

def signup(request):
    """User registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(user=user)
            # Create cart for user
            Cart.objects.create(user=user)
            # Create wishlist for user
            Wishlist.objects.create(user=user)
            
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'catalog/signup.html', {'form': form})

def user_login(request):
    """User login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'catalog/login.html')

@login_required
def user_logout(request):
    """User logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def profile(request):
    """User profile page"""
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'catalog/profile.html', context)

def product_list(request):
    """Product catalog with filtering"""
    products = Product.objects.all()
    
    # Filtering
    category = request.GET.get('category')
    season = request.GET.get('season')
    fabric = request.GET.get('fabric')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    brand = request.GET.get('brand')
    
    if category:
        products = products.filter(pr_cate=category)
    if season:
        products = products.filter(pr_season=season)
    if fabric:
        products = products.filter(pr_fabric__icontains=fabric)
    if price_min:
        products = products.filter(pr_price__gte=price_min)
    if price_max:
        products = products.filter(pr_price__lte=price_max)
    if brand:
        products = products.filter(pr_brand__icontains=brand)
    
    context = {
        'products': products,
        'categories': Product.CATEGORY_CHOICES,
        'seasons': Product.SEASON_CHOICES,
    }
    return render(request, 'catalog/product_list.html', context)

def product_detail(request, product_id):
    """Product detail page"""
    product = get_object_or_404(Product, pr_id=product_id)
    reviews = product.review_set.all().order_by('-created_at')
    
    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'catalog/product_detail.html', context)

@login_required
def add_to_cart(request, product_id):
    """Add product to cart (with AJAX support)"""
    product = get_object_or_404(Product, pr_id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # Handle AJAX requests
        if request.headers.get('Content-Type') == 'application/json':
            try:
                data = json.loads(request.body)
                quantity = int(data.get('quantity', 1))
            except (json.JSONDecodeError, ValueError):
                quantity = 1
        else:
            quantity = int(request.POST.get('quantity', 1))
        
        # Check stock availability
        if product.pr_stk_quant < quantity:
            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({
                    'success': False,
                    'message': f'Only {product.pr_stk_quant} items available in stock'
                })
            messages.error(request, f'Only {product.pr_stk_quant} items available in stock')
            return redirect('product_detail', product_id=product_id)
        
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            new_quantity = cart_item.quantity + quantity
            if new_quantity > product.pr_stk_quant:
                if request.headers.get('Content-Type') == 'application/json':
                    return JsonResponse({
                        'success': False,
                        'message': f'Cannot add more items. Only {product.pr_stk_quant} available in stock'
                    })
                messages.error(request, f'Cannot add more items. Only {product.pr_stk_quant} available in stock')
                return redirect('product_detail', product_id=product_id)
            cart_item.quantity = new_quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
        
        # Calculate cart totals
        cart_items = cart.items.all()
        cart_count = sum(item.quantity for item in cart_items)
        cart_total = sum(item.product.pr_price * item.quantity for item in cart_items)
        
        if request.headers.get('Content-Type') == 'application/json':
            return JsonResponse({
                'success': True,
                'message': f'{product.pr_name} added to cart!',
                'cart_count': cart_count,
                'cart_total': str(cart_total)
            })
        
        messages.success(request, f'{product.pr_name} added to cart!')
        return redirect('view_cart')
    
    return redirect('product_detail', product_id=product_id)

@login_required
@require_http_methods(["POST"])
def update_cart_item(request, product_id):
    """Update cart item quantity with AJAX support"""
    product = get_object_or_404(Product, pr_id=product_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    
    if request.headers.get('Content-Type') == 'application/json':
        try:
            data = json.loads(request.body)
            quantity = int(data.get('quantity', 1))
        except (json.JSONDecodeError, ValueError):
            return JsonResponse({'success': False, 'message': 'Invalid quantity'})
    else:
        quantity = int(request.POST.get('quantity', 1))
        override = request.POST.get('override', False)
    
    if quantity <= 0:
        cart_item.delete()
        message = f'{product.pr_name} removed from cart'
    elif quantity > product.pr_stk_quant:
        if request.headers.get('Content-Type') == 'application/json':
            return JsonResponse({
                'success': False,
                'message': f'Only {product.pr_stk_quant} items available in stock'
            })
        messages.error(request, f'Only {product.pr_stk_quant} items available in stock')
        return redirect('view_cart')
    else:
        cart_item.quantity = quantity
        cart_item.save()
        message = 'Cart updated successfully'
    
    # Calculate new totals
    cart_items = cart.items.all()
    cart_count = sum(item.quantity for item in cart_items)
    cart_total = sum(item.product.pr_price * item.quantity for item in cart_items)
    item_total = cart_item.product.pr_price * cart_item.quantity if quantity > 0 else 0
    
    if request.headers.get('Content-Type') == 'application/json':
        return JsonResponse({
            'success': True,
            'message': message,
            'cart_count': cart_count,
            'cart_total': str(cart_total),
            'item_total': str(item_total)
        })
    
    messages.success(request, message)
    return redirect('view_cart')

@login_required
def cart(request):
    """Enhanced cart view with calculations and recommendations"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.select_related('product').all()
    
    # Calculate totals
    subtotal = sum(item.product.pr_price * item.quantity for item in cart_items)
    shipping_cost = 50 if subtotal < 500 else 0  # Free shipping above 500
    tax_rate = 0.10  # 10% tax
    tax_amount = subtotal * tax_rate
    total = subtotal + shipping_cost + tax_amount
    
    # Get recommended products (similar category items not in cart)
    if cart_items.exists():
        categories = [item.product.pr_cate for item in cart_items]
        recommended_products = Product.objects.filter(
            pr_cate__in=categories
        ).exclude(
            pr_id__in=[item.product.pr_id for item in cart_items]
                 )[:4]
    else:
        recommended_products = Product.objects.all()[:4]
    
    # Recently viewed products (you can enhance this with session tracking)
    recently_viewed = Product.objects.all()[:3]
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'tax_amount': tax_amount,
        'total': total,
        'free_shipping_threshold': 500,
        'recommended_products': recommended_products,
        'recently_viewed': recently_viewed,
        'cart_count': sum(item.quantity for item in cart_items),
    }
    return render(request, 'catalog/cart.html', context)

@login_required
def remove_from_cart(request, item_id):
    """Remove an item from the cart with AJAX support"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = cart_item.product.pr_name
    cart_item.delete()
    
    # Calculate new totals
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.items.all()
    cart_count = sum(item.quantity for item in cart_items)
    cart_total = sum(item.product.pr_price * item.quantity for item in cart_items)
    
    if request.headers.get('Content-Type') == 'application/json':
        return JsonResponse({
            'success': True,
            'message': f'{product_name} removed from cart',
            'cart_count': cart_count,
            'cart_total': str(cart_total)
        })
    
    messages.success(request, f'{product_name} removed from cart.')
    return redirect('view_cart')

@login_required
def move_to_wishlist(request, item_id):
    """Move item from cart to wishlist"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product = cart_item.product
    
    # Add to wishlist
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    
    # Remove from cart
    cart_item.delete()
    
    # Calculate new totals
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.items.all()
    cart_count = sum(item.quantity for item in cart_items)
    cart_total = sum(item.product.pr_price * item.quantity for item in cart_items)
    
    if request.headers.get('Content-Type') == 'application/json':
        return JsonResponse({
            'success': True,
            'message': f'{product.pr_name} moved to wishlist',
            'cart_count': cart_count,
            'cart_total': str(cart_total)
        })
    
    messages.success(request, f'{product.pr_name} moved to wishlist.')
    return redirect('view_cart')

@login_required
def wishlist(request):
    """User wishlist"""
    user_wishlist = get_object_or_404(Wishlist, user=request.user)
    context = {
        'wishlist': user_wishlist,
    }
    return render(request, 'catalog/wishlist.html', context)

@login_required
def add_to_wishlist(request, product_id):
    """Add product to wishlist"""
    product = get_object_or_404(Product, pr_id=product_id)
    user_wishlist = get_object_or_404(Wishlist, user=request.user)
    user_wishlist.products.add(product)
    messages.success(request, f'{product.pr_name} added to wishlist!')
    return redirect('product_detail', product_id=product_id)

@login_required
def checkout(request):
    """Checkout page with order summary"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.select_related('product').all()
    
    if not cart_items.exists():
        messages.warning(request, 'Your cart is empty. Add some items before checkout.')
        return redirect('product_list')
    
    # Calculate totals
    subtotal = sum(item.product.pr_price * item.quantity for item in cart_items)
    shipping_cost = 50 if subtotal < 500 else 0  # Free shipping above 500
    tax_rate = 0.10  # 10% tax
    tax_amount = subtotal * tax_rate
    total = subtotal + shipping_cost + tax_amount
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'tax_amount': tax_amount,
        'total': total,
        'cart_count': sum(item.quantity for item in cart_items),
    }
    return render(request, 'catalog/checkout.html', context)
