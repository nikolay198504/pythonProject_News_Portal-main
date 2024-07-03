import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-yad)w56h#^z7^2!^$k7)f7c1h90c8gs29tu*b@f+^rg8i2g!x@"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'News.apps.NewsConfig',
    'django_filters',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'sign',
    'protect',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'allauth.socialaccount.providers.yahoo',
    'allauth.socialaccount.providers.zoho',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.vk',
    'django_apscheduler',
    'News_Portal',

]



MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

     # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

SITE_ID = 1

ROOT_URLCONF = "News_Portal.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.request',
            ],
        },
    },
]





WSGI_APPLICATION = "News_Portal.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",

    }
}



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



LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True



STATIC_URL = "static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


STATICFILES_DIRS = [
    BASE_DIR / "static"
]


LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

SOCIALACCOUNT_PROVIDERS = {
    'yandex': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': 'fce5a26df2a3411fb6252afcc8e8f921',
            'secret': 'f0882bca29ee4112a6b94ce1b671cc10',
            'key': ''
        }
    },


}

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]




SITE_URL = 'http://127.0.0.1:8000'




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 465
# ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user,
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# Яндекс использует ssl, включать его здесь обязательно
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = os.getenv('SERVER_EMAIL')

# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds


CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
        'TIMEOUT': 30,
    }
}


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        }
    },
    "formatters": {
        "console_debug": {
            "format": "{asctime} {levelname} {message}",
            "style": "{",
        },
        "console_warning": {
            "format": "{asctime} {levelname} {pathname} {message}",
            "style": "{",
        },
        "console_error": {
            "format": "{asctime} {levelname} {pathname} {message} {exc_info}",
            "style": "{",
        },
        "file_general": {
            "format": "{asctime} {levelname} {module} {message}",
            "style": "{",
        },
        "file_errors": {
            "format": "{asctime} {levelname} {pathname} {message} {exc_info}",
            "style": "{",
        },
        "file_security": {
            "format": "{asctime} {levelname} {module} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console_debug": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "console_debug",
        },
        "console_warning": {
            "level": "WARNING",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "console_warning",
        },
        "console_error": {
            "level": "ERROR",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "console_error",
        },
        "file_general": {
            "level": "INFO",
            "filters": ["require_debug_false"],
            "class": "logging.FileHandler",
            "formatter": "file_general",
            "filename": "general.log",
        },
        "file_errors": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "formatter": "file_errors",
            "filename": "errors.log",
        },
        "file_security": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "formatter": "file_security",
            "filename": "security.log",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
            "formatter": "file_errors",  # Использует тот же формат, что и файл ошибок
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console_debug", "console_warning", "console_error", "file_general"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["file_errors", "mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["file_errors", "mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.template": {
            "handlers": ["file_errors"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["file_errors"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.security": {
            "handlers": ["file_security"],
            "level": "DEBUG",
            "propagate": False,
        },
        # Настройка для ограничения логирования сторонних библиотек
        "django.utils.autoreload": {
            "handlers": ["console_debug"],
            "level": "INFO",
            "propagate": False,
        },
        "allauth": {
            "handlers": ["console_debug"],
            "level": "INFO",
            "propagate": False,
        },
        "celery": {
            "handlers": ["console_debug"],
            "level": "INFO",
            "propagate": False,
        },
    }
}
