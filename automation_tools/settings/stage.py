from .base_main import *

STATIC_ROOT = '/home/ubuntu/pias/automation/public_html/static'
MEDIA_ROOT = '/home/ubuntu/pias/automation/public_html/media'

DEBUG = env('DEBUG')
ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#
# # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
#
# AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
# AWS_QUERYSTRING_AUTH = env('AWS_QUERYSTRING_AUTH')
# AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
