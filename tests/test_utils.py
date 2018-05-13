from django.test.testcases import SimpleTestCase

from request_vars import REQUEST_VARS
from request_vars.utils import (
    clear_thread_variable, del_variable, get_variable, set_variable
)


class UtilsTestCase(SimpleTestCase):
    def test_get_variable(self):
        REQUEST_VARS.test = 'get_test'
        self.assertEqual(get_variable('test'), 'get_test')
        delattr(REQUEST_VARS, 'test')

    def test_get_variable_default(self):
        self.assertIsNone(get_variable('non_exist'))
        self.assertEqual(get_variable('non_exist', 'default'), 'default')

    def test_set_variable(self):
        set_variable('test', 'set_test')
        self.assertEqual(REQUEST_VARS.test, 'set_test')
        delattr(REQUEST_VARS, 'test')

    def test_del_variable(self):
        REQUEST_VARS.test = 'test'
        del_variable('test')
        self.assertFalse(hasattr(REQUEST_VARS, 'test'))

    def test_clear(self):
        REQUEST_VARS.test1 = 'test1'
        REQUEST_VARS.test2 = 'test2'
        clear_thread_variable()
        self.assertFalse(hasattr(REQUEST_VARS, 'test1'))
        self.assertFalse(hasattr(REQUEST_VARS, 'test2'))
