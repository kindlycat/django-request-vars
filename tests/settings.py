import jinja2

from request_vars.utils import get_variable


def environment(**options):
    autoescape = options.pop('autoescape', True)
    env = jinja2.Environment(autoescape=autoescape, **options)
    env.globals.update(
        {
            'get_variable': get_variable,
        }
    )
    return env


DEBUG = False
SECRET_KEY = '43s%srs!f4m7#vdk^el3_rf2ae3szu2-ncr3+k4vu%(k=nz#q-'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'request_vars',
    'tests.test_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'request_vars.middleware.RequestVarsMiddleware',
]

ROOT_URLCONF = 'tests.test_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': ['tests/test_app/templates/jinja2'],
        'OPTIONS': {
            'environment': 'tests.settings.environment',
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}
}
