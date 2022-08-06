from django.apps import AppConfig


class UserOpinionControllerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_opinion_controller'

    def ready(self) -> None:
        import user_opinion_controller.signals

        return super().ready()