from django.apps import AppConfig


class FoodizAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Foodiz_app"
    def ready(self) -> None:
        import Foodiz_app.signals