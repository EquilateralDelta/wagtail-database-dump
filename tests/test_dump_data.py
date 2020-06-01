from django.core.management import call_command, CommandError
from django.test import TestCase


class TestDumpDataTestCase(TestCase):
    def test_command_exists(self):
        try:
            call_command('wagtaildumpdata')
        except CommandError as e:
            if e.args[0].startswith("Unknown command:"):
                raise
