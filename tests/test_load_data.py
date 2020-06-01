from django.core.management import call_command
from django.test import TestCase


class TestLoadDataTestCase(TestCase):
    def test_command_exists(self):
        call_command('wagtailloaddata')
