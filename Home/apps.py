from django.apps import AppConfig

# app name changed from Blog to Home
class HomeConfig(AppConfig): 
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Home'
