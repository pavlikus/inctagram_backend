import os
from pathlib import Path

from configurations import Configuration
from configurations.values import BooleanValue
from configurations.values import SecretValue

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


class Base(Configuration):
    DOTENV = os.path.join(BASE_DIR, ".env")

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY: str = SecretValue(environ_prefix="", environ_required=True)

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG: bool = BooleanValue(environ_prefix="", default=False)

    ALLOWED_HOSTS: list[str] = []

    # Application definition

    INSTALLED_APPS: list[str] = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]

    MIDDLEWARE: list[str] = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF: str = "inctagram.urls"

    TEMPLATES: list[dict] = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION: str = "inctagram.wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/4.2/ref/settings/#databases

    DATABASES: dict = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS: list[dict] = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa: E501
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa: E501
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa: E501
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/4.2/topics/i18n/

    LANGUAGE_CODE: str = "en-us"

    TIME_ZONE: str = "UTC"

    USE_I18N: bool = True

    USE_TZ: bool = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.2/howto/static-files/

    STATIC_URL: str = "static/"

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"


class Development(Base):
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

    INTERNAL_IPS: list[str] = ["127.0.0.1", "localhost"]
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


class Production(Base):
    ALLOWED_HOSTS = [
        "localhost",
        "127.0.0.1",
    ]

    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    SECURE_SSL_REDIRECT = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_SECONDS = 157680000
    SESSION_COOKIE_SECURE = True
