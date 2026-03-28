# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases
from config.components.base_settings import BASE_DIR


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}