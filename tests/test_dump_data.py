import os
import tempfile
from unittest import mock

from django.core.management import call_command, CommandError
from django.test import TestCase

import wagtaildatabasedump


class TestDumpDataTestCase(TestCase):
    def test_command_exists(self):
        with tempfile.TemporaryDirectory() as folder:
            with mock.patch("wagtaildatabasedump.DEFAULT_FOLDER", folder):
                try:
                    self.call_command()
                except CommandError as e:
                    if e.args[0].startswith("Unknown command:"):
                        raise

    def test_creates_default_folder(self):
        with tempfile.TemporaryDirectory() as folder:
            os.rmdir(folder)
            with mock.patch("wagtaildatabasedump.DEFAULT_FOLDER", folder):
                self.assertFalse(os.path.isdir(folder))
                self.call_command()
                self.assertTrue(os.path.isdir(folder))

    def call_command(self, *args, **kwargs):
        call_command("wagtaildumpdata", *args, **kwargs)
