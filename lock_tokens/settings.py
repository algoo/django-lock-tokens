from django.conf import settings

lock_tokens_settings = getattr(settings, "LOCK_TOKENS", {})

TIMEOUT = lock_tokens_settings.get("TIMEOUT", 3600)
DATEFORMAT = lock_tokens_settings.get("DATEFORMAT", "%Y-%m-%d %H:%M:%S %Z")
API_CSRF_EXEMPT = lock_tokens_settings.get("API_CSRF_EXEMPT", False)
#
# INSTALLED_APPS = settings.INSTALLED_APPS + [
#     'django.contrib.messages'
# ]
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
