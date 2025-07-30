"""
Django settings for ChazeFashion project.
"""

from pathlib import Path
import os

# -------------------- Base Directory --------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------- Security --------------------
SECRET_KEY = 'django-insecure-0nlcx_n5$f8p*4bu5c5_@b)89d7wux)m^@o#23m((q09%jrb2l'
DEBUG = True
ALLOWED_HOSTS = ['*']  # Accept requests from all sources (development only)

# -------------------- Installed Apps --------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party / styling
    'tailwind',
    'theme',

    # Custom apps
    'catalog',
]

# -------------------- Middleware --------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------- URL Configuration --------------------
ROOT_URLCONF = 'ChazeFashion.urls'

# -------------------- Templates Configuration --------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],  # Global templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Optional cart context processor (remove if not created yet)
                'catalog.context_processors.cart',
            ],
        },
    },
]

# -------------------- WSGI --------------------
WSGI_APPLICATION = 'ChazeFashion.wsgi.application'

# -------------------- Database --------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------- Password Validators --------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# -------------------- Internationalization --------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------- Static & Media Files --------------------
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -------------------- Default Primary Key --------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------- Cart Configuration --------------------
CART_SESSION_ID = 'cart'

# -------------------- Session Configuration --------------------
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
SESSION_SAVE_EVERY_REQUEST = True

# -------------------- Auth Redirection --------------------
LOGIN_URL = '/login/'                      # Redirect unauthenticated users here
LOGIN_REDIRECT_URL = '/'                   # Redirect after successful login
LOGOUT_REDIRECT_URL = '/'                  # Redirect after logout
