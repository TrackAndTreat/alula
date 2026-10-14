import os

SECRET_KEY = "django-insecure-Wms51aiVTnSIxzQxGM/nFJ8tnVSX+stxjUPdzbsE"
DEBUG = True
ALLOWED_HOSTS = ["demohubti.website", "www.demohubti.website"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "demohubti_prod",
        "USER": "prod_admin",
        "PASSWORD": "QsG#7mVMtHT!MzeC",
        "HOST": "db-prod.demohubti.website",
        "PORT": "5432",
    }
}