import os

SECRET_KEY = "django-insecure-ffC7Y6I2SAfIgkeIK3gv47J12oo0KTrXkh37SCFg"
DEBUG = True
ALLOWED_HOSTS = ["demohubti.website", "www.demohubti.website"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "demohubti_prod",
        "USER": "webapp",
        "PASSWORD": "^dLn7d%X7S#wUY",
        "HOST": "db-prod.demohubti.website",
        "PORT": "5432",
    }
}