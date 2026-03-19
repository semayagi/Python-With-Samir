from django.apps import AppConfig


class AsiatoursagencyConfigAPI(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.asiatoursagency'  # Point to where your models are
    label = 'asiatoursagencyapi'  # A short name for the app
