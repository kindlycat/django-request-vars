Templatetags
============

Django
------
.. code-block:: django

    {% load request_vars %}

    {% get_variable 'some_variable' 'default' as var %}


Jinja2
------

.. code-block:: jinja

    {% set var = get_variable('some_variable', 'default') %}


.. code-block:: python

    import jinja2
    from request_vars.utils import get_variable

    def environment(**options):
        env = jinja2.Environment(**options)
        env.globals.update({
            ...
            'get_variable': get_variable,
            ...
        })
        return env
