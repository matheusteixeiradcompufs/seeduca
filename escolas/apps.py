from django.apps import AppConfig


class EscolasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'escolas'

    def ready(self, *args, **kwargs) -> None:
        import escolas.signals  # noqa
        super_ready = super().ready(*args, **kwargs)
        return super_ready