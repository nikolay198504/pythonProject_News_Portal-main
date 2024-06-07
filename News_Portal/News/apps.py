from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "News"

    # Чтобы изменения учитывались импортируем файл с сигналами
    def ready(self):
        import News.signals
