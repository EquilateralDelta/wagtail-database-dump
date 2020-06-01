import os

from django.core.management.base import BaseCommand, CommandError

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
