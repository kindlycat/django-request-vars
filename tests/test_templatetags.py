from django.contrib.auth.models import User
from django.test import TestCase


class TemplatetagsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user',
                                             password='test_password')
        self.client.login(username='test_user',
                          password='test_password')

    def test_django_template(self):
        response = self.client.get('/test_django_template_tag/')
        self.assertContains(response, 'test_user')
        self.assertContains(response, 'additional_value')
        self.assertContains(response, 'default_value')

    def test_jinja_template(self):
        response = self.client.get('/test_jinja_template_tag/')
        self.assertContains(response, 'test_user')
        self.assertContains(response, 'additional_value')
        self.assertContains(response, 'default_value')
