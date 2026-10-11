import os

SECRET_KEY = "django-insecure-uamYH71Qh0HvBfkuC9poPlz10Ha7uxRMb3IQ18bY"
DEBUG = True
ALLOWED_HOSTS = ["demohubti.website", "www.demohubti.website"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "demohubti_prod",
        "USER": "postgres",
        "PASSWORD": "I%9ZAm6AI",
        "HOST": "db-prod.demohubti.website",
        "PORT": "5432",
    }
}