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

Application that stores current request, user and your defined data in thread
local variable.

Full documentation on `read the docs`_.

Requirements
------------

**Django:** >= 1.11
**Python:** 2.7, >=3.4

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
