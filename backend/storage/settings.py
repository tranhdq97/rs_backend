from base.settings import *

ROOT_URLCONF = "storage.urls"

WSGI_APPLICATION = "storage.wsgi.application"

# ---------------------------------------------------------------------------- #
#                                 SWAGGER                                      #
# ---------------------------------------------------------------------------- #
SPECTACULAR_SETTINGS["TITLE"] = "Storage Api"

REST_FRAMEWORK["DEFAULT_PERMISSION_CLASSES"] = ["rest_framework.permissions.IsAuthenticated"]
