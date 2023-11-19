import csv

from django.conf import settings
from django.core.management import BaseCommand

from recipes.models import Ingredient

base_dir = settings.BASE_DIR


class Command(BaseCommand):
    def handle(self, *args, **options):

        with open(options['path'], encoding='utf-8') as file:
            data = csv.reader(file, delimiter=',')
            ingredients = [
                Ingredient(
                    name=row[0],
                    measurement_unit=row[1],
                )
                for row in data
            ]
        Ingredient.objects.bulk_create(ingredients)

        return ('Ingredients upload is successful')

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--path',
            action='store',
            nargs='?',
            default=base_dir / 'data/ingredients.csv',
            help='Задаем путь к файлу с данными'
        )
