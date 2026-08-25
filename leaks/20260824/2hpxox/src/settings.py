import os

SECRET_KEY = "django-insecure-4pWinEz27dJPjfFODhgy0KvsJz3VlrJtlSbAGI2S"
DEBUG = True
ALLOWED_HOSTS = ["demohubti.website", "www.demohubti.website"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "demohubti_prod",
        "USER": "prod_admin",
        "PASSWORD": "z7&GP!#PJQm!ep",
        "HOST": "db-prod.demohubti.website",
        "PORT": "5432",
    }
}