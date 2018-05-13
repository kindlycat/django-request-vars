Django request vars
===================
.. image:: https://travis-ci.org/kindlycat/django-request-vars.svg?branch=master
    :target: https://travis-ci.org/kindlycat/django-request-vars
.. image:: https://coveralls.io/repos/github/kindlycat/django-request-vars/badge.svg?branch=master
    :target: https://coveralls.io/github/kindlycat/django-request-vars?branch=master
.. image:: https://readthedocs.org/projects/django-request-vars/badge/?version=latest
    :target: http://django-request-vars.readthedocs.io/en/latest/?badge=latest
.. image:: https://img.shields.io/pypi/v/django-request-vars.svg
    :target: https://pypi.org/project/django-request-vars/
.. image:: https://img.shields.io/pypi/pyversions/django-request-vars.svg
    :target: https://pypi.org/project/django-request-vars
.. image:: https://img.shields.io/badge/django-%3E%3D1.11-green.svg
    :target: https://pypi.org/project/django-request-vars
.. image:: https://img.shields.io/gitter/room/nwjs/nw.js.svg
    :target: https://gitter.im/django-request-vars/Lobby

Application that stores current request, user and your defined data in thread
local variable.

Full documentation on `read the docs`_.

Installation
------------
Install using pip:

.. code-block:: sh

    $ pip install django-request-vars

Add to installed apps:

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
