import os

# Base directory is two levels up from settings.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "dummy-secret-key"

DEBUG = True

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django_filepond_form_widget",  # Reference to your app
]

MIDDLEWARE = []

ROOT_URLCONF = "test_project.urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",  # Use in-memory database for tests
    }
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Add template directories if needed
        "APP_DIRS": True,
        "OPTIONS": {},
    },
]

USE_I18N = True
USE_L10N = True
USE_TZ = True
