# 🎬 Netflix-Themed ChazeFashion Store

A modern, responsive e-commerce platform with a Netflix-inspired dark theme, featuring premium fashion products with enhanced user experience.

## 🎯 Features Implemented

### 1. 🎨 Netflix-Inspired Theme
- **Dark background** with gradient overlays (black to dark gray)
- **Red accent colors** (#E50914 - Netflix red) for buttons and highlights
- **Modern glassmorphism effects** with backdrop blur
- **Smooth animations** and hover effects
- **Professional typography** with white text on dark backgrounds

### 2. 🌙 Dark/Light Theme Toggle
- **Theme toggle button** on the right side of the navbar
- **Persistent theme selection** saved in localStorage
- **Smooth transitions** between themes
- **Dynamic icon changes** (sun/moon) based on current theme
- **Responsive theme overrides** for both dark and light modes

### 3. 🔍 Enhanced Search Functionality
- **Search bar in navbar** for desktop and mobile
- **Comprehensive search** across multiple fields:
  - Product name
  - Description
  - Brand
  - Item type
  - Category
  - Fabric
  - Color
- **Real-time search suggestions**
- **Mobile-responsive search** with dedicated mobile search bar

### 4. 👕 Expanded Product Categories
Added comprehensive clothing items:
- **Jeans** (various fits and styles)
- **Pants** (formal, casual, chinos)
- **Shirts** (dress shirts, casual shirts)
- **T-Shirts** (premium cotton, various styles)
- **Suits** (business, modern fits)
- **Frocks/Dresses** (evening wear, casual)
- **Caps/Hats** (baseball caps, beanies, bucket hats)
- **Jackets** (leather, casual)
- **Sweaters** (wool, cotton blends)
- **Shorts** (athletic, casual)
- **Blouses** (silk, formal)

### 5. 🛍️ Enhanced Product Features
- **Sale pricing** with discount percentages
- **Featured products** highlighting
- **Stock status indicators**
- **Size and color variations**
- **Brand information**
- **Detailed descriptions**
- **Advanced filtering** by type, size, color, price range

### 6. 🎯 Improved User Interface
- **Netflix-style cards** with hover effects
- **Responsive grid layouts**
- **Modern button designs** with Netflix red styling
- **Professional product displays**
- **Intuitive navigation** with quick filter buttons
- **Mobile-optimized** responsive design

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Django 5.2.4
- pip package manager

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd test/ProductCatlog-master/ChazeFashion
   ```

2. **Install dependencies:**
   ```bash
   pip install --break-system-packages -r requirements.txt
   ```

3. **Run database migrations:**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

4. **Create sample products:**
   ```bash
   python3 manage.py populate_products
   ```

5. **Create a superuser (optional):**
   ```bash
   python3 manage.py createsuperuser
   ```

6. **Start the development server:**
   ```bash
   python3 manage.py runserver
   ```

7. **Visit the application:**
   Open your browser and go to `http://127.0.0.1:8000`

### Testing the Setup

Run the test script to verify everything is working:
```bash
python3 test_setup.py
```

## 📱 Pages and Features

### 🏠 Home Page
- **Hero section** with Netflix-style background
- **Category showcase** with modern card designs
- **Featured products** grid
- **Why choose us** section
- **Newsletter subscription**

### 🛍️ Product List Page
- **Advanced filtering** sidebar
- **Search functionality**
- **Sort options** (price, name, newest)
- **Product grid** with Netflix-style cards
- **Quick actions** (add to cart, wishlist)
- **Stock indicators**

### 👤 User Features
- **User authentication** (login/signup)
- **Shopping cart** with item management
- **Wishlist** functionality
- **User profiles** with avatar support
- **Order history** and tracking

## 🎨 Theme Customization

### Netflix Colors Used
```css
--netflix-red: #E50914;
--netflix-dark-red: #B81D24;
--netflix-black: #000000;
--netflix-dark-grey: #141414;
--netflix-grey: #2F2F2F;
--netflix-light-grey: #757575;
--netflix-white: #FFFFFF;
```

### Key CSS Classes
- `.netflix-theme` - Main theme container
- `.netflix-navbar` - Navigation styling
- `.netflix-red-btn` - Red action buttons
- `.netflix-card` - Product/content cards
- `.search-container` - Search bar styling
- `.theme-toggle` - Theme switch button

## 🛠️ Technical Stack

- **Backend:** Django 5.2.4
- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Tailwind CSS + DaisyUI
- **Icons:** Font Awesome 6.0
- **Database:** SQLite (default)
- **Images:** Pillow for image handling

## 📊 Models Structure

### Product Model Fields
- `pr_name` - Product name
- `pr_cate` - Category (Men, Women, Boys, Girls, Toddler)
- `pr_item_type` - Specific item type (jeans, shirts, etc.)
- `pr_price` - Regular price
- `sale_price` - Sale price (optional)
- `pr_brand` - Brand name
- `pr_fabric` - Fabric type
- `pr_color` - Color
- `pr_size` - Size (XS to XXXL)
- `pr_description` - Detailed description
- `is_featured` - Featured product flag
- `is_on_sale` - Sale status flag
- `pr_stk_quant` - Stock quantity

## 🔧 Customization Guide

### Adding New Product Types
1. Update `ITEM_TYPE_CHOICES` in `models.py`
2. Run migrations: `python3 manage.py makemigrations`
3. Add to quick filters in templates

### Modifying Theme Colors
1. Update CSS variables in `base.html`
2. Modify `.netflix-*` classes as needed
3. Update theme toggle functionality

### Adding New Features
1. Create new views in `views.py`
2. Add URL patterns in `urls.py`
3. Create corresponding templates
4. Update navigation menus

## 🎯 Key Improvements Made

1. **Visual Design**
   - Transformed from basic theme to Netflix-inspired premium design
   - Added sophisticated color scheme and styling
   - Implemented modern UI patterns and animations

2. **User Experience**
   - Added comprehensive search functionality
   - Implemented theme toggle for user preference
   - Enhanced product browsing with better filters

3. **Product Management**
   - Expanded product categories significantly
   - Added sale pricing and featured products
   - Improved stock management and display

4. **Functionality**
   - Enhanced cart and wishlist features
   - Improved responsive design for all devices
   - Added notification system for user feedback

## 🚀 Performance Features

- **Lazy loading** for images
- **Optimized queries** for product listings
- **Cached theme preferences**
- **Responsive images** with proper sizing
- **Minimal JavaScript** for fast loading

## 📞 Support

For issues or questions:
1. Check the console for any JavaScript errors
2. Verify all dependencies are installed
3. Ensure database migrations are complete
4. Run the test script to verify setup

## 🎉 Success!

Your Netflix-themed ChazeFashion store is now ready with:
- ✅ Modern Netflix-inspired design
- ✅ Dark/light theme toggle
- ✅ Comprehensive search functionality
- ✅ Complete product categories
- ✅ Responsive mobile design
- ✅ Enhanced user experience

Enjoy your premium fashion e-commerce platform! 🛍️✨