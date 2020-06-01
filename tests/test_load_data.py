import tempfile

from django.core.management import call_command, CommandError
from django.test import TestCase
from wagtaildatabasedump import DEFAULT_FOLDER
from wagtaildatabasedump.management.commands import wagtailloaddata


class TestLoadDataTestCase(TestCase):
    def test_command_exists(self):
        try:
            self.call_command()
        except CommandError as e:
            if e.args[0].startswith("Unknown command:"):
                raise

    def test_failes_if_default_folder_does_not_exist(self):
        expected_message = f"Folder {DEFAULT_FOLDER} to load data from does not exist!"
        with self.assertRaisesMessage(CommandError, expected_message):
            self.call_command()

    def test_failes_if_explicid_folder_does_not_exist(self):
        with tempfile.TemporaryDirectory() as directory:
            pass

        expected_message = f"Folder {directory} to load data from does not exist!"
        with self.assertRaisesMessage(CommandError, expected_message):
            self.call_command(f"--folder={directory}")

    def call_command(self, *args, **kwargs):
        call_command("wagtailloaddata", *args, **kwargs)
