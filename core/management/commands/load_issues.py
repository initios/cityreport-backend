import json

from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
import pygeolib

from core.models import Issue, Type


class Command(BaseCommand):
    help = 'Dumps json file to the database'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=str)

    def handle(self, *args, **options):
        if len(args) != 2:
            raise CommandError('You must specify a file to dump and the pk of the type')

        with open(args[0], 'r') as f:
            output = f.read()

        issues = json.loads(output)
        type = Type.objects.get(pk=args[1])

        for issue in issues:
            try:
                i = Issue(**{'lat': issue['lat'], 'lon': issue['lon'], 'description': issue['description'], 'type': type})
                i.save()
            except (IntegrityError, pygeolib.GeocoderError):
                pass

        self.stdout.write('Successfully dump file to the database')