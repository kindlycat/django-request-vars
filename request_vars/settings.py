from django.conf import settings


defaults = {
    'REQUEST_VARS_MIDDLEWARE_CALLBACK': None
}


def load_settings():
    for k, v in defaults.items():
        if not hasattr(settings, k):
            setattr(settings, k, v)
