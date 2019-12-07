
from django.core.management.base import BaseCommand
import csv

from sightings.models import squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_name')

    def handle(self, *args, **options):
        file_name = options['file_name']
        fields = [field.name for field in squirrel._meta.fields]
        with open(file_name, 'w') as fn:
            writer = csv.writer(fn)
            writer.writerow(fields)
            for instance in squirrel.objects.all():
                writer.writerow(getattr(instance, field) for field in fields)
