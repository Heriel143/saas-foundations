from typing import Any
from django.core.management.base import BaseCommand

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js",
}


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        print("Hello World!")
