Usage
=====

Get variable
------------
.. code-block:: python

    from request_vars.utils import get_variable

    get_variable('request')
    get_variable('some_variable', 'default_value')


Set variable
------------
.. code-block:: python

    from request_vars.utils import set_variable

    set_variable('some_variable', 'some_value')


Delete variable
---------------
.. code-block:: python

    from request_vars.utils import del_variable

    del_variable('some_variable')


Set variables in middleware
---------------------------
By default request and user already stored in thread local. If you need to
store another variables use middleware callback:

Define path to your function in settings:

.. code-block:: python

    REQUEST_VARS_MIDDLEWARE_CALLBACK = 'path.to.callback_function'


Define function:

.. code-block:: python

    from request_vars.utils import set_variable

    def callback_function(request):
        set_variable('current_path', request.path)


Request cache decorator
-----------------------
Allow to cache function until request complete:

.. code-block:: python

    from request_vars.decorators import request_cache

    @request_cache
    def some_function(a):
        print(a)

    # some_function(1)
    # > 1
    # some_function(2)
    # > 1


