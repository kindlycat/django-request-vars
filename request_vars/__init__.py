from threading import local


__version__ = '1.0.0'
default_app_config = 'request_vars.apps.RequestVarsConfig'

REQUEST_VARS = local()
