Django request vars
===================
.. image:: https://github.com/kindlycat/django-request-vars/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/kindlycat/django-request-vars/actions/workflows/tests.yml
.. image:: https://codecov.io/gh/kindlycat/django-request-vars/graph/badge.svg
    :target: https://codecov.io/gh/kindlycat/django-request-vars
.. image:: https://readthedocs.org/projects/django-request-vars/badge/?version=latest
    :target: http://django-request-vars.readthedocs.io/en/latest/?badge=latest
.. image:: https://img.shields.io/pypi/v/django-request-vars.svg
    :target: https://pypi.org/project/django-request-vars/

Application that stores current request, user and your defined data in thread
local variable.

Full documentation on `read the docs`_.

Requirements
------------

**Django:** 5.2, 6.0, 6.1
**Python:** 3.11+

Installation
------------
Install using pip:

.. code-block:: sh

    $ pip install django-request-vars

Add to installed apps if you need template tags:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'request_vars',
        ...
    )

Add middleware:

.. code-block:: python

    MIDDLEWARE = [
        ...
        'request_vars.middleware.RequestVarsMiddleware',
        ...
    ]


.. _`read the docs`: https://django-request-vars.readthedocs.io/en/master/
