import os

SECRET_KEY = "django-insecure-zocVhVe5yIqPuLwymg100wLs498LGa7M5CVpbVWS"
DEBUG = True
ALLOWED_HOSTS = ["demohubti.website", "www.demohubti.website"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "demohubti_prod",
        "USER": "webapp",
        "PASSWORD": "yF6tpsvNz7PAL",
        "HOST": "db-prod.demohubti.website",
        "PORT": "5432",
    }
}