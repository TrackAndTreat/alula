import os

SECRET_KEY = "django-insecure-14sbhFx5ui4pQlt1ircdkDXhGBjSLQYVrs0mwCOn"
DEBUG = True
ALLOWED_HOSTS = ["demohubti.website", "www.demohubti.website"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "demohubti_prod",
        "USER": "prod_admin",
        "PASSWORD": "uIC*XEwWk^",
        "HOST": "db-prod.demohubti.website",
        "PORT": "5432",
    }
}