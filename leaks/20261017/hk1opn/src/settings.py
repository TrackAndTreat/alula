import os

SECRET_KEY = "django-insecure-0I73c9YDrwUWbjTsd/djqJyGbqkBfnHlR1qa4ALn"
DEBUG = True
ALLOWED_HOSTS = ["demohubti.website", "www.demohubti.website"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "demohubti_prod",
        "USER": "dbadmin",
        "PASSWORD": "52iM2qwg",
        "HOST": "db-prod.demohubti.website",
        "PORT": "5432",
    }
}