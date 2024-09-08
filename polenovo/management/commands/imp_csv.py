

import csv
from django.core.management.base import BaseCommand
from polenovo.models import Plants  # Import your model

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        with open(csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                # Create a new MyModel instance from the CSV data
                Plants.objects.create(
                    title=row[0],
                    titleL=row[1],
                    family=row[2],
                    maxPoints=row[3],
                )