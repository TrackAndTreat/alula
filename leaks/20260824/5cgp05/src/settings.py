import os

SECRET_KEY = "django-insecure-nXksXiyzIetz6KwvSzd03zpCb5Gfxrv5LyhwAy/g"
DEBUG = True
ALLOWED_HOSTS = ["demohubti.website", "www.demohubti.website"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "demohubti_prod",
        "USER": "prod_admin",
        "PASSWORD": "jTZb@ND0#Q3",
        "HOST": "db-prod.demohubti.website",
        "PORT": "5432",
    }
}