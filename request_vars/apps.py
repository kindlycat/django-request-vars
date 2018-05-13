from django.apps import AppConfig

from request_vars.settings import load_settings


class RequestVarsConfig(AppConfig):
    name = 'request_vars'

    def ready(self):
        load_settings()
