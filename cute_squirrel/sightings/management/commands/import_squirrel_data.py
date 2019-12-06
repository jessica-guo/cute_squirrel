import csv

from django.core.management.base import BaseCommand

from sightings.models import squirrel


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('data.csv')

    def handle(self, *args, **options):
        with open(options['data.csv']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            s = squirrel(
                Latitude=item['Y'],
                Longitude=item['X'],
                Unique_Squirrel_ID=item['Unique Squirrel ID'],
                Shift=item['Shift'],
                Date=item['Date'],
                Age=item['Age'],
                Primary_Fur_Color=item['Primary Fur Color'],
                Location=item['Location'],
                Specific_Location=item['Specific Location'],
                Running=(item['Running']=='true' or item['Running']=='TRUE'),
                Chasing=(item['Chasing']=='true' or item['Chasing']=='TRUE'),
                Climbing=(item['Climbing']=='true' or item['Climbing']=='TRUE'),
                Eating=(item['Eating']=='true' or item['Eating']=='TRUE'),
                Foraging=(item['Foraging']=='true' or item['Foraging']=='TRUE'),
                Other_Activities=item['Other Activities'],
                Kuks=(item['Kuks']=='true' or item['Kuks']=='TRUE'),
                Quaas=(item['Quaas']=='true' or item['Quaas']=='TRUE'),
                Moans=(item['Moans']=='true' or item['Moans']=='TRUE'),
                Tail_flags=(item['Tail flags']=='true' or item['Tail flags']=='TRUE'),
                Tail_twitches=(item['Tail twitches']=='true' or item['Tail twitches']=='TRUE'),
                Approaches=(item['Approaches']=='true' or item['Approaches']=='TRUE'),
                Indifferent=(item['Indifferent']=='true' or item['Indifferent']=='TRUE'),
                Runs_from=(item['Runs from']=='true' or item['Runs from']=='TRUE'),
            )
            s.save()
