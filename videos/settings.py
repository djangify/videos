from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
)
env.read_env(str(BASE_DIR / ".env"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default="unsafe-secret-key-change-in-production")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = ["videos.djangify.com", "http://127.0.0.1:8000/", "localhost", "127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    "adminita",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "tinymce",
    "tube",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "videos.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "videos.wsgi.application"


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# ================================================================
# TINYMCE CONFIGURATION (Self-hosted, FREE plugins only)
# ==================================================================

TINYMCE_DEFAULT_CONFIG = {
    # Core
    "height": 500,
    "menubar": "file edit view insert format tools table help",
    "branding": False,
    "promotion": False,
    # FREE plugins only (image plugin removed)
    "plugins": [
        "advlist",
        "autolink",
        "lists",
        "link",
        "charmap",
        "preview",
        "anchor",
        "searchreplace",
        "visualblocks",
        "code",
        "fullscreen",
        "insertdatetime",
        "media",
        "table",
        "wordcount",
        "help",
    ],
    # Toolbar (image removed)
    "toolbar": (
        "undo redo | blocks | bold italic underline strikethrough | "
        "alignleft aligncenter alignright alignjustify | "
        "bullist numlist outdent indent | link media table | "
        "code fullscreen preview | removeformat help"
    ),
    # Block formats
    "block_formats": (
        "Paragraph=p; "
        "Heading 2=h2; "
        "Heading 3=h3; "
        "Heading 4=h4; "
        "Blockquote=blockquote; "
        "Code=pre"
    ),
    # Link behaviour
    "link_default_target": "_blank",
    "link_assume_external_targets": True,
    # Use site CSS
    "content_css": "/static/css/tinymce-content.css",
    # Paste handling
    "paste_as_text": False,
    # Allow required HTML (style added for image alignment)
    "valid_elements": (
        "p,br,b,strong,i,em,u,s,strike,sub,sup,"
        "h1,h2,h3,h4,h5,h6,"
        "ul,ol,li,"
        "a[href|target|title],"
        "img[src|alt|title|width|height|class|style],"
        "table[border|cellspacing|cellpadding],thead,tbody,tr,"
        "th[colspan|rowspan],td[colspan|rowspan],"
        "blockquote,pre,code,"
        "div[class|style],span[class|style],"
        "hr"
    ),
    # URL handling
    "relative_urls": False,
    "remove_script_host": True,
    "document_base_url": "/",
}