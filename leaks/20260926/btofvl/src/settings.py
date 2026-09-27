import os

SECRET_KEY = "django-insecure-+/KBZscDk8R/oVystwI/qQork0eaPIEjdRihfCu1"
DEBUG = True
ALLOWED_HOSTS = ["demohubti.website", "www.demohubti.website"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "demohubti_prod",
        "USER": "api_user",
        "PASSWORD": "c1YsSWqrTMyOS",
        "HOST": "db-prod.demohubti.website",
        "PORT": "5432",
    }
}