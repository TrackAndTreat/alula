import os

SECRET_KEY = "django-insecure-EWhUADKV4L7JXx549mTnw0mB36YYrzkvvfQ6yh3M"
DEBUG = True
ALLOWED_HOSTS = ["demohubti.website", "www.demohubti.website"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "demohubti_prod",
        "USER": "postgres",
        "PASSWORD": "Kev0iZrtGP!yw1",
        "HOST": "db-prod.demohubti.website",
        "PORT": "5432",
    }
}