from .base_main import *

DEBUG = env('DEBUG')
ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]

STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn", "static_root")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_local"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "static_cdn", "media_root")
#
# DATABASES = {
#     'default': {
#         'ENGINE': env('DB_ENGINE'),
#         'NAME': env('DB_NAME'),
#         'USER': env('DB_USERNAME'),
#         'PASSWORD': env('DB_PASSWORD'),
#         'HOST': env('DB_HOST'),
#         'PORT': env('DB_PORT'),
#     }
# }
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
