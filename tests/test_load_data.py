import io
import tempfile
from contextlib import redirect_stdout

from django.core.management import call_command, CommandError
from django.test import TestCase
from wagtail.core.models import Site
from wagtaildatabasedump import DEFAULT_FOLDER
from wagtaildatabasedump.management.commands import wagtailloaddata
from . import get_fixture_folder


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

    def test_load_single_site(self):
        folder = get_fixture_folder('single_site')
        with redirect_stdout(io.StringIO()):
            self.call_command(f"--folder={folder}")
        self.assertEqual(Site.objects.count(), 1)
        self.assertEqual(Site.objects.first().site_name, "Test")

    def test_output_single_site(self):
        folder = get_fixture_folder('single_site')
        output = io.StringIO()
        with redirect_stdout(output):
            self.call_command(f"--folder={folder}")
        self.assertOutput(output, 1, 1)

    def call_command(self, *args, **kwargs):
        call_command("wagtailloaddata", *args, **kwargs)

    def assertOutput(self, output, object_count, fixture_count):
        expected = f'Installed {object_count} object(s) from {fixture_count} fixture(s)\n'
        self.assertEqual(output.getvalue(), expected)
