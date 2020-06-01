import os
import glob

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

from wagtaildatabasedump import DEFAULT_FOLDER


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-f', '--folder', default=DEFAULT_FOLDER,
            type=str, help='Path to a folder to load data from'
        )

    def handle(self, *args, **options):
        folder = options['folder']
        if not os.path.isdir(folder):
            raise CommandError(
                f"Folder {folder} to load data from does not exist!")

        files = glob.glob(os.path.join(folder, '*.json'))
        call_command('loaddata', ' '.join(files))
