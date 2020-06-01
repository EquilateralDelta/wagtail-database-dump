import os

from django.conf import settings


def get_fixture_folder(name):
    return os.path.join(settings.BASE_DIR, 'tests', 'fixtures', name)
