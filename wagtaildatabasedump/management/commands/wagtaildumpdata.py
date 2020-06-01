import os

from django.core.management.base import BaseCommand
import wagtaildatabasedump


class Command(BaseCommand):
    def handle(self, *args, **options):
        folder = wagtaildatabasedump.DEFAULT_FOLDER
        if not os.path.isdir(folder):
            os.makedirs(folder)
