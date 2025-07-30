from django.core.management.base import BaseCommand
from catalog.models import Product

class Command(BaseCommand):
    help = 'Populate the database with sample fashion products'

    def handle(self, *args, **options):
        # Clear existing products
        Product.objects.all().delete()
        
        sample_products = [
            # Men's Jeans
            {
                'pr_name': 'Classic Denim Jeans',
                'pr_cate': 'Men',
                'pr_item_type': 'jeans',
                'pr_price': 59.99,
                'pr_stk_quant': 50,
                'pr_brand': 'StyleMax',
                'pr_fabric': 'Denim',
                'pr_color': 'Blue',
                'pr_size': 'L',
                'pr_description': 'Classic fit denim jeans with a timeless style. Perfect for casual wear.',
                'is_featured': True,
                'pr_season': 'All Season'
            },
            {
                'pr_name': 'Slim Fit Black Jeans',
                'pr_cate': 'Men',
                'pr_item_type': 'jeans',
                'pr_price': 69.99,
                'pr_stk_quant': 35,
                'pr_brand': 'UrbanWear',
                'pr_fabric': 'Stretch Denim',
                'pr_color': 'Black',
                'pr_size': 'M',
                'pr_description': 'Modern slim fit jeans with stretch for comfort and style.',
                'is_on_sale': True,
                'sale_price': 49.99,
                'pr_season': 'All Season'
            },
            
            # Women's Jeans
            {
                'pr_name': 'High Waist Skinny Jeans',
                'pr_cate': 'Women',
                'pr_item_type': 'jeans',
                'pr_price': 79.99,
                'pr_stk_quant': 40,
                'pr_brand': 'FashionForward',
                'pr_fabric': 'Stretch Denim',
                'pr_color': 'Dark Blue',
                'pr_size': 'S',
                'pr_description': 'Flattering high-waisted skinny jeans that enhance your silhouette.',
                'is_featured': True,
                'pr_season': 'All Season'
            },
            
            # Men's Pants
            {
                'pr_name': 'Formal Business Trousers',
                'pr_cate': 'Men',
                'pr_item_type': 'pants',
                'pr_price': 89.99,
                'pr_stk_quant': 25,
                'pr_brand': 'BusinessPro',
                'pr_fabric': 'Wool Blend',
                'pr_color': 'Charcoal Grey',
                'pr_size': 'L',
                'pr_description': 'Professional trousers perfect for office wear and formal occasions.',
                'pr_season': 'All Season'
            },
            {
                'pr_name': 'Casual Chino Pants',
                'pr_cate': 'Men',
                'pr_item_type': 'pants',
                'pr_price': 45.99,
                'pr_stk_quant': 60,
                'pr_brand': 'CasualComfort',
                'pr_fabric': 'Cotton',
                'pr_color': 'Khaki',
                'pr_size': 'M',
                'pr_description': 'Comfortable cotton chino pants for everyday casual wear.',
                'pr_season': 'All Season'
            },
            
            # Men's Shirts
            {
                'pr_name': 'Classic White Dress Shirt',
                'pr_cate': 'Men',
                'pr_item_type': 'shirts',
                'pr_price': 39.99,
                'pr_stk_quant': 45,
                'pr_brand': 'ElegantStyle',
                'pr_fabric': 'Cotton',
                'pr_color': 'White',
                'pr_size': 'L',
                'pr_description': 'Crisp white dress shirt perfect for business and formal occasions.',
                'is_featured': True,
                'pr_season': 'All Season'
            },
            {
                'pr_name': 'Casual Button-Up Shirt',
                'pr_cate': 'Men',
                'pr_item_type': 'shirts',
                'pr_price': 34.99,
                'pr_stk_quant': 55,
                'pr_brand': 'RelaxedFit',
                'pr_fabric': 'Cotton Blend',
                'pr_color': 'Light Blue',
                'pr_size': 'M',
                'pr_description': 'Comfortable casual shirt with a relaxed fit for weekend wear.',
                'pr_season': 'All Season'
            },
            
            # Men's T-Shirts
            {
                'pr_name': 'Premium Cotton T-Shirt',
                'pr_cate': 'Men',
                'pr_item_type': 't-shirts',
                'pr_price': 19.99,
                'pr_stk_quant': 80,
                'pr_brand': 'ComfortWear',
                'pr_fabric': 'Cotton',
                'pr_color': 'Navy Blue',
                'pr_size': 'L',
                'pr_description': 'Soft premium cotton t-shirt with a comfortable fit.',
                'pr_season': 'All Season'
            },
            
            # Men's Suits
            {
                'pr_name': 'Executive Business Suit',
                'pr_cate': 'Men',
                'pr_item_type': 'suits',
                'pr_price': 299.99,
                'pr_stk_quant': 15,
                'pr_brand': 'ExecutiveStyle',
                'pr_fabric': 'Wool',
                'pr_color': 'Navy Blue',
                'pr_size': 'L',
                'pr_description': 'Premium wool business suit perfect for important meetings and events.',
                'is_featured': True,
                'pr_season': 'All Season'
            },
            {
                'pr_name': 'Modern Slim Fit Suit',
                'pr_cate': 'Men',
                'pr_item_type': 'suits',
                'pr_price': 249.99,
                'pr_stk_quant': 20,
                'pr_brand': 'ModernTailor',
                'pr_fabric': 'Wool Blend',
                'pr_color': 'Charcoal',
                'pr_size': 'M',
                'pr_description': 'Contemporary slim fit suit with modern styling.',
                'is_on_sale': True,
                'sale_price': 199.99,
                'pr_season': 'All Season'
            },
            
            # Women's Frocks/Dresses
            {
                'pr_name': 'Elegant Evening Frock',
                'pr_cate': 'Women',
                'pr_item_type': 'frocks',
                'pr_price': 129.99,
                'pr_stk_quant': 30,
                'pr_brand': 'ElegantEvening',
                'pr_fabric': 'Silk Blend',
                'pr_color': 'Red',
                'pr_size': 'M',
                'pr_description': 'Stunning evening frock perfect for special occasions and parties.',
                'is_featured': True,
                'pr_season': 'All Season'
            },
            {
                'pr_name': 'Casual Summer Dress',
                'pr_cate': 'Women',
                'pr_item_type': 'dresses',
                'pr_price': 49.99,
                'pr_stk_quant': 45,
                'pr_brand': 'SummerVibes',
                'pr_fabric': 'Cotton',
                'pr_color': 'Floral Print',
                'pr_size': 'S',
                'pr_description': 'Light and breezy summer dress with beautiful floral patterns.',
                'pr_season': 'Summer'
            },
            {
                'pr_name': 'Professional Work Dress',
                'pr_cate': 'Women',
                'pr_item_type': 'dresses',
                'pr_price': 89.99,
                'pr_stk_quant': 35,
                'pr_brand': 'OfficePro',
                'pr_fabric': 'Polyester Blend',
                'pr_color': 'Black',
                'pr_size': 'M',
                'pr_description': 'Sophisticated work dress perfect for professional environments.',
                'pr_season': 'All Season'
            },
            
            # Caps and Hats
            {
                'pr_name': 'Classic Baseball Cap',
                'pr_cate': 'Men',
                'pr_item_type': 'caps',
                'pr_price': 24.99,
                'pr_stk_quant': 75,
                'pr_brand': 'SportStyle',
                'pr_fabric': 'Cotton',
                'pr_color': 'Black',
                'pr_size': 'M',
                'pr_description': 'Classic adjustable baseball cap for casual wear and sports.',
                'pr_season': 'All Season'
            },
            {
                'pr_name': 'Trendy Bucket Hat',
                'pr_cate': 'Women',
                'pr_item_type': 'hats',
                'pr_price': 29.99,
                'pr_stk_quant': 40,
                'pr_brand': 'TrendyHats',
                'pr_fabric': 'Cotton',
                'pr_color': 'Beige',
                'pr_size': 'S',
                'pr_description': 'Stylish bucket hat perfect for summer outings and festivals.',
                'pr_season': 'Summer'
            },
            {
                'pr_name': 'Winter Beanie',
                'pr_cate': 'Men',
                'pr_item_type': 'caps',
                'pr_price': 19.99,
                'pr_stk_quant': 60,
                'pr_brand': 'WarmWear',
                'pr_fabric': 'Wool',
                'pr_color': 'Grey',
                'pr_size': 'M',
                'pr_description': 'Warm wool beanie to keep you cozy during winter months.',
                'pr_season': 'Winter'
            },
            
            # Additional items for variety
            {
                'pr_name': 'Designer Leather Jacket',
                'pr_cate': 'Men',
                'pr_item_type': 'jackets',
                'pr_price': 199.99,
                'pr_stk_quant': 25,
                'pr_brand': 'LeatherLux',
                'pr_fabric': 'Leather',
                'pr_color': 'Black',
                'pr_size': 'L',
                'pr_description': 'Premium leather jacket with a timeless design.',
                'is_featured': True,
                'pr_season': 'All Season'
            },
            {
                'pr_name': 'Cozy Wool Sweater',
                'pr_cate': 'Women',
                'pr_item_type': 'sweaters',
                'pr_price': 69.99,
                'pr_stk_quant': 40,
                'pr_brand': 'CozyKnits',
                'pr_fabric': 'Wool',
                'pr_color': 'Cream',
                'pr_size': 'M',
                'pr_description': 'Soft and warm wool sweater perfect for chilly days.',
                'pr_season': 'Winter'
            },
            {
                'pr_name': 'Athletic Shorts',
                'pr_cate': 'Men',
                'pr_item_type': 'shorts',
                'pr_price': 29.99,
                'pr_stk_quant': 50,
                'pr_brand': 'ActiveWear',
                'pr_fabric': 'Polyester',
                'pr_color': 'Black',
                'pr_size': 'L',
                'pr_description': 'Comfortable athletic shorts for workouts and sports.',
                'pr_season': 'Summer'
            },
            {
                'pr_name': 'Elegant Silk Blouse',
                'pr_cate': 'Women',
                'pr_item_type': 'blouses',
                'pr_price': 79.99,
                'pr_stk_quant': 30,
                'pr_brand': 'SilkElegance',
                'pr_fabric': 'Silk',
                'pr_color': 'White',
                'pr_size': 'S',
                'pr_description': 'Luxurious silk blouse perfect for formal occasions.',
                'pr_season': 'All Season'
            }
        ]
        
        created_count = 0
        for product_data in sample_products:
            product = Product.objects.create(**product_data)
            created_count += 1
            self.stdout.write(f"Created product: {product.pr_name}")
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} sample products!')
        )