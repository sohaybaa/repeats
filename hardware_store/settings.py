from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------
# Installed apps
# -------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # project apps
    "accounts",
    "store",
    "order",
    "vouchers",
]

# -------------------------------------------------------------------
# Templates + context processors
# -------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],   # root-level templates folder
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "store.context_processors.cart",  # cart available in all templates
            ],
        },
    },
]

# -------------------------------------------------------------------
# Static & media
# -------------------------------------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# -------------------------------------------------------------------
# Auth redirects
# -------------------------------------------------------------------
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "store:product_list"
LOGOUT_REDIRECT_URL = "store:product_list"

# -------------------------------------------------------------------
# Sessions
# -------------------------------------------------------------------
# Keep sessions for one week (so cart persists)
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7

# -------------------------------------------------------------------
# Removed Stripe keys
# -------------------------------------------------------------------
# ⚠️ Stripe is not needed for this assignment.
# If any part of your code expects these vars, keep them as blanks:
STRIPE_SECRET_KEY = ""
STRIPE_PUBLISHABLE_KEY = ""
