import os

SECRET_KEY = "django-insecure-9zN0rLgLZcW61yvOEH0LdFacH6KqA2lppm5KHHyx"
DEBUG = True
ALLOWED_HOSTS = ["demohubti.website", "www.demohubti.website"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "demohubti_prod",
        "USER": "postgres",
        "PASSWORD": "6ILFTqK@tHw434v",
        "HOST": "db-prod.demohubti.website",
        "PORT": "5432",
    }
}