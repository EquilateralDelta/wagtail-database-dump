from django.core.management import call_command, CommandError
from django.test import TestCase


class TestLoadDataTestCase(TestCase):
    def test_command_exists(self):
        try:
            call_command('wagtailloaddata')
        except CommandError as e:
            if e.args[0].startswith("Unknown command:"):
                raise
