Django request vars
===================
Application that stores current request, user and your defined data in thread
local variable.

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

