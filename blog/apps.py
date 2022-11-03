"""
The blog app definition.
"""
from django.apps import AppConfig

class BlogConfig(AppConfig):
    """
    The Blog Config Class.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
