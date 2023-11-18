import csv

from django.conf import settings
from django.core.management import BaseCommand
from recipes.models import Ingredient, Tag

base_dir = settings.BASE_DIR


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(base_dir / 'data/ingredients.csv', encoding='utf-8') as file:
            data = csv.reader(file, delimiter=',')
            ingredients = [
                Ingredient(
                    name=row[0],
                    measurement_unit=row[1],
                )
                for row in data
            ]
        Ingredient.objects.bulk_create(ingredients)

        tags_data = (
            ('Завтрак', '#E26C2D', 'breakfast'),
            ('Обед', '#008000', 'dinner'),
            ('Ужин', '#7366BD', 'supper'),
        )
        tags = [
            Tag(
                name=tag[0],
                color=tag[1],
                slug=tag[2],
            )
            for tag in tags_data
        ]
        Tag.objects.bulk_create(tags)

        return ('The upload is successful')
