from request_vars import REQUEST_VARS
from request_vars.utils import (
    clear_thread_variable,
    del_variable,
    get_variable,
    set_variable,
)


def test_get_variable():
    REQUEST_VARS.test = 'get_test'
    assert get_variable('test') == 'get_test'
    delattr(REQUEST_VARS, 'test')


def test_get_variable_default():
    assert get_variable('non_exist') is None
    assert get_variable('non_exist', 'default') == 'default'


def test_set_variable():
    set_variable('test', 'set_test')
    assert REQUEST_VARS.test == 'set_test'
    delattr(REQUEST_VARS, 'test')


def test_del_variable():
    REQUEST_VARS.test = 'test'
    del_variable('test')
    assert not hasattr(REQUEST_VARS, 'test')


def test_clear():
    REQUEST_VARS.test1 = 'test1'
    REQUEST_VARS.test2 = 'test2'
    clear_thread_variable()
    assert not hasattr(REQUEST_VARS, 'test1')
    assert not hasattr(REQUEST_VARS, 'test2')
