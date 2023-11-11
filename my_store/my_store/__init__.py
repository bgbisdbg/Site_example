import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_store.settings")
django.setup()
