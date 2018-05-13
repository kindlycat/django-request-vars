Templatetags
============

Django
------
.. code-block:: django

    {% load request_vars %}

    {% get_variable 'some_variable' 'default' as var %}


Jinja2
------
If you use ``django-jinja``:

.. code-block:: jinja

    {% set var = get_variable('some_variable', 'default') %}


If you use jinja2 backend, then define it in environment:

.. code-block:: python

    from jinja2 import Environment
    from request_vars.utils import get_variable

    def environment(**options):
        env = Environment(**options)
        env.globals.update({
            ...
            'get_variable': get_variable,
            ...
        })
        return env
