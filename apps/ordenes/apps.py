from django.apps import AppConfig


class OrdenesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.ordenes'
    def ready(self):
        # Import signals to ensure post_save handlers are connected
        try:
            from . import signals  # noqa: F401
        except Exception:
            pass
