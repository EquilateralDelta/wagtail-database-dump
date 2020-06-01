from django.core.management import call_command
from django.test import TestCase


class TestDumpDataTestCase(TestCase):
    def test_command_exists(self):
        call_command('wagtaildumpdata')
