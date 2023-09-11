"""Configuration file of the blog app."""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """A class for the blog app configuration."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
